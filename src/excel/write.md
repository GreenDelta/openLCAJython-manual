# Write

The example below shows how to create an Excel file and write its first cell.

```python
from java.io import FileOutputStream
from org.apache.poi.ss.usermodel import WorkbookFactory

# Path where the Excel file will be written
PATH = "/path/to/file.xlsx"

# Load the workbook from the file
workbook = WorkbookFactory.create(True)

# Create a new sheet
sheet = workbook.createSheet()

# Create the first row (index 0) and first cell (index 0)
# and set a string value inside it
row = sheet.createRow(0)
cell = row.createCell(0)
cell.setCellValue("Hello from openLCA!")

# Write the workbook content to the file
output_stream = FileOutputStream(PATH)
workbook.write(output_stream)

# Close the output stream to ensure data is properly saved
output_stream.close()

# Close the workbook to free resources
workbook.close()
```
