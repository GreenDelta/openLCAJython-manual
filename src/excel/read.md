# Read

The following code snippet shows how to open an Excel file and read the first cell of the first
sheet:

```python
from java.io import File
from org.apache.poi.ss.usermodel import WorkbookFactory

# read an Excel file from the following path
PATH = "/path/to/file.xlsx"

# load the workbook from the file
workbook = WorkbookFactory.create(File(PATH))

# get the first sheet (indices are 0 based)
sheet = workbook.getSheetAt(0)

# use the Excel utility to read values from the sheet
# the indices of rows and columns are 0 based
row = 0
column = 0
# read a string value from a cell
string = Excel.getString(sheet, row, column)
print("String value of cell A1: %s" % string)

# read a numeric value from a cell
number = Excel.getDouble(sheet, row + 1, column + 1)
print("Numeric value of cell B2: %d" % number)

# close the workbook to clean up resources
workbook.close()

# refresh the navigator (it does not do anything in this example as nothing was inserted into the
# database)
App.runInUI("Refresh navigator", lambda: Navigator.refresh())
```
