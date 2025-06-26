import string

from java.io import FileInputStream, FileOutputStream, IOException
from org.apache.poi.xssf.usermodel import XSSFCell, XSSFSheet, XSSFWorkbook

PATH_TO_EXCEL_FILE = "/path/to/excel_automation.xlsx"
IMPACT_METHOD_ID = "67371e90-e11b-44e2-b7aa-039816c4e281"


def write(path, callback):  # type: (str, Callable[[XSSFWorkbook], None]) -> None
    stream = None
    wb = None
    try:
        stream = FileInputStream(path)

        wb = XSSFWorkbook(stream)
        callback(wb)

        wb.write(FileOutputStream(path))
    except IOException as e:
        print("Error", e)
    finally:
        try:
            if stream is not None:
                stream.close()
            if wb is not None:
                wb.close()
        except:
            pass


def get_cell(sheet, column, row):  # type: (XSSFSheet, str, int) -> XSSFCell
    column_label = string.ascii_uppercase.index(column)
    return sheet.getRow(row).getCell(column_label)


def get_string_cell(sheet, column, row):  # type: (XSSFSheet, str, int) -> str
    return get_cell(sheet, column, row).getStringCellValue()


def get_numeric_cell(sheet, column, row):  # type: (XSSFSheet, str, int) -> float
    return get_cell(sheet, column, row).getNumericCellValue()


def get_process_info(wb):  # wb: XSSFWorkbook -> Generator[dict[str, str or float]]:
    sheet = wb.getSheet("Processes")
    for i in range(1, sheet.getLastRowNum() + 1):
        name = get_string_cell(sheet, "A", i)
        uuid = get_string_cell(sheet, "B", i)
        amount = get_numeric_cell(sheet, "C", i)
        yield {"name": name, "uuid": uuid, "amount": amount}


def product_system_from_process(uuid):  # type: (str) -> ProductSystem
    process = db.get(Process, uuid)
    if not isinstance(process, Process):
        raise Exception("Process not found")

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


def get_or_create_sheet(wb, name):  # type: (XSSFWorkbook, str) -> XSSFSheet
    sheet = wb.getSheet(name)
    if sheet is None:
        return wb.createSheet(name)
    else:
        return sheet


def write_impacts_to_sheet(
    sheet, impacts
):  # type: (XSSFSheet, Generator[dict[str, float or str]]) -> None
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


def print_process_info(wb):
    for process in get_process_info(wb):
        print(process)


def run_calculations(wb):
    for process in get_process_info(wb):
        print("Running impact calculation for %s..." % process["name"])
        for impact in impacts_of(process):
            print(
                "The total impact on %s is %.4f %s."
                % (impact["name"], impact["value"], impact["unit"])
            )


def write_results(wb):
    for process in get_process_info(wb):
        sheet = get_or_create_sheet(wb, process["name"])
        print("Running impact calculation for %s..." % process["name"])
        write_impacts_to_sheet(sheet, impacts_of(process))
    print("Done")


write(PATH_TO_EXCEL_FILE, write_results)
