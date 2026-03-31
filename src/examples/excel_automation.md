# Excel automation

This example shows how a tedious task can be automated using a spreadsheet and Jython.

Our use case is the following:

- We have a spreadsheet with a list of processes and their UUIDs.
- We want to create a product system for each process and run impact calculations on it.
- We want to store the results in a new sheet in the same spreadsheet.

An example spreadsheet can be downloaded [here](excel_automation.xlsx). It provides a list of
processes from the _ecoinvent v3.10.1 APOS_ database.

To follow this example with the full script, copy the content of this [file](excel_automation.py).

## Open the spreadsheet and gather the UUIDs

Checkout the [Integration with Excel](../user_guide/excel) chapter for more details about how to
open the spreadsheet.

The following code snippet will read the processes' name, UUIDS and amounts from the first sheet
named "Processes". The callback function will print the process information to the console.

```python
import string

from java.io import FileInputStream, FileOutputStream
from org.apache.poi.ss.usermodel import WorkbookFactory


# Do not forget to edit this path to point to your XLSX file!
PATH = "/path/to/excel/excel_automation.xlsx"

# Load the workbook from the file (using FileInputStream to be able to later write to it)
input_stream = FileInputStream(PATH)
workbook = WorkbookFactory.create(input_stream)

# Get the Processes sheet
sheet = workbook.getSheet("Processes")


# This function is an helper to use the cell names (A1, B1, C1, etc.) instead of their index
def get_cell(sheet, column, row):  # type: (XSSFSheet, str, int) -> XSSFCell
    column_label = string.ascii_uppercase.index(column)
    return sheet.getRow(row).getCell(column_label)


def get_string_cell(sheet, column, row):  # type: (XSSFSheet, str, int) -> str
    return get_cell(sheet, column, row).getStringCellValue()


def get_numeric_cell(sheet, column, row):  # type: (XSSFSheet, str, int) -> float
    return get_cell(sheet, column, row).getNumericCellValue()


def get_process_info(sheet):  # sheet: XSSFSheet -> Generator[dict[str, str or float]]:
    for i in range(1, sheet.getLastRowNum() + 1):
        name = get_string_cell(sheet, "A", i)
        amount = get_numeric_cell(sheet, "B", i)
        uuid = get_string_cell(sheet, "C", i)
        yield {"name": name, "amount": amount, "uuid": uuid}


for process in get_process_info(sheet):
    print(process)

workbook.close()
```

## Create product systems and run impact calculations

Now that we have access the processes information, we can modify the script so that we create
product systems and run impact calculations on them. The following code snippet will create a
product system for each process and run impact calculations on it. The results are then printed to
the console.

```python
IMPACT_METHOD_ID = "67371e90-e11b-44e2-b7aa-039816c4e281"

def product_system_from_process(uuid):  # type: (str) -> ProductSystem
    process = db.get(Process, uuid)
    if not isinstance(process, Process):
        raise Exception("Process not found: " + uuid)

    config = (
        LinkingConfig()
        .providerLinking(ProviderLinking.PREFER_DEFAULTS)
        .preferredType(LinkingConfig.PreferredType.UNIT_PROCESS)
    )

    return ProductSystemBuilder(db, config).build(process)


def result_of_system(system, amount):  # type: (ProductSystem, float) -> Result
    method = db.get(ImpactMethod, IMPACT_METHOD_ID)
    setup = CalculationSetup.of(system).withAmount(amount).withImpactMethod(method)

    return SystemCalculator(db).calculate(setup)


def impacts_of(
    process,
):  # type: (dict[str, str or float]) -> Generator[dict[str, float or str]]
    system = product_system_from_process(process["uuid"])
    result = result_of_system(system, process["amount"])
    for impact in result.getTotalImpacts():
        yield {
            "name": impact.impact().name,
            "value": impact.value(),
            "unit": impact.impact().referenceUnit,
        }

def run_calculations(sheet):
    for process in get_process_info(sheet):
        print("Running impact calculation for %s..." % process["name"])
        for impact in impacts_of(process):
            print(
                "The total impact on %s is %.4f %s."
                % (impact["name"], impact["value"], impact["unit"])
            )

run_calculations(sheet)
```

## Store the results in a new sheet

Now that we have the results, we can store them in sheets. Let's modify the callback function so
that it creates a new sheet for each process and stores the results in it.

```python
def get_or_create_sheet(workbook, name):  # type: (XSSFWorkbook, str) -> XSSFSheet
    sheet = workbook.getSheet(name)
    if sheet is None:
        return workbook.createSheet(name)
    else:
        return sheet


def write_impacts_to_sheet(
    sheet, impacts
):  # type: (XSSFSheet, dict[str, float or str]) -> None
    row = sheet.createRow(0)
    row.createCell(0).setCellValue("Name")
    row.createCell(1).setCellValue("Value")
    row.createCell(2).setCellValue("Unit")

    for i, impact in enumerate(impacts):
        row = sheet.createRow(i + 1)
        row.createCell(0).setCellValue(impact["name"])
        row.createCell(1).setCellValue(impact["value"])
        row.createCell(2).setCellValue(impact["unit"])

    for i in range(3):
        sheet.autoSizeColumn(i)


for process in get_process_info(sheet):
    sheet = get_or_create_sheet(workbook, process["name"])
    print("Running impact calculation for %s..." % process["name"])
    impacts = list(impacts_of(process))
    write_impacts_to_sheet(sheet, impacts)

# Write the workbook content to the file
output_stream = FileOutputStream(PATH)
workbook.write(output_stream)

# Close the input and output streams to ensure data is properly saved
input_stream.close()
output_stream.close()

# Close the workbook to free resources
workbook.close()

print("Done")
```
