# Integration with Excel

### Read the value of a cell

The following code snippet shows how to open an Excel file and read the first cell of the first
sheet:

```python
from java.io import File
from org.apache.poi.ss.usermodel import WorkbookFactory

# This example reads an Excel file from this path
PATH = "/path/to/file.xlsx"

# Load the workbook from the file
workbook = WorkbookFactory.create(File(PATH))

# Get the first sheet (indices are 0 based)
sheet = workbook.getSheetAt(0)

# Now you can use the Excel utility to read values from the sheet
# again, the indices of rows and columns are 0 based
row = 0
column = 0
# Reading a string value from a cell
string = Excel.getString(sheet, row, column)
print("String value of cell A1: %s" % string)

# Reading a numeric value from a cell
number = Excel.getDouble(sheet, row + 1, column + 1)
print("Numeric value of cell B2: %d" % number)

# Finally, it is good to close the workbook to clean up resources
workbook.close()
```

### Write one cell

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
