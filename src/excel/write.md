# Write

The example below shows how to create an Excel file and write its first cell.

```python
from java.io import FileOutputStream
from org.apache.poi.ss.usermodel import WorkbookFactory

# path where the Excel file will be written
PATH = "/path/to/file.xlsx"

# load the workbook from the file
workbook = WorkbookFactory.create(True)

# create a new sheet
sheet = workbook.createSheet()

# create the first row (index 0) and first cell (index 0)
# and set a string value inside it
row = sheet.createRow(0)
cell = row.createCell(0)
cell.setCellValue("Hello from openLCA!")

# write the workbook content to the file
output_stream = FileOutputStream(PATH)
workbook.write(output_stream)

# close the output stream to ensure data is properly saved
output_stream.close()

# close the workbook to free resources
workbook.close()
```
