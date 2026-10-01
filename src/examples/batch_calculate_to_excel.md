# Batch calculate to Excel

This recipe calculates **every product system** in the database under one impact method and writes the
total impact per category to an Excel file — one row per product system, one column per impact
category.

```python
from java.io import FileOutputStream
from org.apache.poi.ss.usermodel import WorkbookFactory

# where the results will be written
PATH = "/path/to/results.xlsx"

# the impact method used for every calculation
method = db.getForName(ImpactMethod, "AWARE")
categories = list(method.impactCategories)

# create a workbook and a sheet
workbook = WorkbookFactory.create(True)
sheet = workbook.createSheet("Results")

# header row: one column per impact category
header = sheet.createRow(0)
header.createCell(0).setCellValue("Product system")
for col, category in enumerate(categories):
    header.createCell(col + 1).setCellValue(
        "%s [%s]" % (category.name, category.referenceUnit)
    )

# one row per product system
for i, system in enumerate(ProductSystemDao(db).getAll()):
    setup = CalculationSetup.of(system).withImpactMethod(method)
    result = SystemCalculator(db).calculate(setup)

    row = sheet.createRow(i + 1)
    row.createCell(0).setCellValue(system.name)
    for col, category in enumerate(categories):
        value = result.getTotalImpactValueOf(Descriptor.of(category))
        row.createCell(col + 1).setCellValue(value)

    # free the result memory before the next calculation
    result.dispose()

# write the workbook to the file and close everything
output_stream = FileOutputStream(PATH)
workbook.write(output_stream)
output_stream.close()
workbook.close()

print("Wrote results for %d product systems to %s" % (sheet.getLastRowNum(), PATH))
```
