# Read

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
