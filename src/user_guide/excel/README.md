# Integration with CSV and Excel

A repetitive task that openLCA practitioners face is the conversion of the results of a calculation
into a CSV file that can be imported into Excel or any other spreadsheet program. Similarly, it is
also a common task to import a CSV file into openLCA. This section shows you how to do this using
Jython.

## Read the value of a cell

To import a spreadsheet file into openLCA, you can use the Java package XSSF that is part of
openLCA. The package allows to read and write Excel files using the
[Apache POI](https://poi.apache.org/) library. The following code snippet shows how to open an Excel
file and read the first cell of the first sheet:

```python
from java.io import File
from org.apache.poi.ss.usermodel import WorkbookFactory

# This example would read an Excel file from this path
PATH = "/path/to/file.xlsx"

# Load the workbook from the file
workbook = WorkbookFactory.create(File(PATH))

# Get the first sheet (indices are 0 based)
sheet = workbook.getSheetAt(0)

# Now you can use the Excel utility to read values from the sheet
# again, the indices of rows and columns are 0 based
row = 0
column = 0
# This would read a string value from a cell
string = Excel.getString(sheet, row, column)
print("String value of cell A1: %s" % string)

# And this would read a numeric value from a cell
number = Excel.getDouble(sheet, row + 1, column + 1)
print("Numeric value of cell B2: %d" % number)

# finally, it is good to close the workbook to clean up resources
workbook.close()
```

### Write one cell

To export a spreadsheet file from openLCA, you can use the same package XSSF that is part of
openLCA.

```python
from java.io import FileOutputStream
from org.apache.poi.xssf.usermodel import XSSFWorkbook

# Path where the Excel file will be written
path = "/path/to/file.xlsx"

# Create a new Excel workbook (XLSX format)
workbook = XSSFWorkbook()

# Create a new sheet named "Sheet2"
sheet = workbook.createSheet("Sheet2")

# Create the first row (index 0) and first cell (index 0)
# and set a string value inside it
row = sheet.createRow(0)
cell = row.createCell(0)
cell.setCellValue("Hello from openLCA!")

# Write the workbook content to the file
output_stream = FileOutputStream(path)
workbook.write(output_stream)

# Close the output stream to ensure data is properly saved
output_stream.close()

# Close the workbook to free resources
workbook.close()
```

### Optional make an Excel class

To make your life easier, you can create a class that encapsulates the above code. This way, you can
use the class to read and write Excel files. Simply create a file `excel.py` in your user directory
(`~/openLCA-data-1.4/python`) and add the following code:

```python
from java.io import FileInputStream, FileOutputStream, IOException
from org.apache.poi.xssf.usermodel import XSSFWorkbook


class Excel:

    def __init__(self, path):
        self.path = path

    def _execute(
        self, callback, write
    ):  # callback: function(XSSFWorkbook), write: boolean
        stream = None
        wb = None
        try:
            stream = FileInputStream(self.path)

            wb = XSSFWorkbook(stream)
            callback(wb)

            if write:
                wb.write(FileOutputStream(self.path))
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

    def read(self, callback):  # callback: function(XSSFWorkbook)
        self._execute(callback, False)

    def write(self, callback):  # callback: function(XSSFWorkbook)
        self._execute(callback, True)
```

Now you can use the `Excel` class to read and write Excel files. To reproduce the above examples,
simply use the following code:

```python
from excel import Excel


# Do not forget to edit this path to point to your XLSX file!
PATH_TO_EXCEL_FILE = '/path/to/file.xlsx'
excel = Excel(PATH_TO_EXCEL_FILE)

def print_first_cell(wb):  # wb: XSSFWorkbook
    cell = wb.getSheetAt(0).getRow(0).getCell(0)
    print("Content of cell A1: %s" % cell.getStringCellValue())

def hello(wb):  # wb: XSSFWorkbook
    sheet = wb.createSheet("Sheet2")
    sheet.createRow(0).createCell(0).setCellValue("Hello from openLCA!")

excel.read(print_first_cell)
excel.write(hello)
```
