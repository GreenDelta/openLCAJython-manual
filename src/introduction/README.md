# Introduction

Welcome to the world of scripting in [openLCA](https://www.openlca.org/)!

openLCA is written in Java. It includes a tool for automation and customization:
[Jython](http://www.jython.org/). Jython is a version of Python 2.7 that runs on Java. It lets you
write Python code that works inside openLCA.

To start, go to: `Tools → Developer Tools → Python`.

This opens the built-in Python editor. There, you can write and run scripts to automate tasks, add
small custom features, or test ideas.

![Open the Python editor](open_python_editor.png)

To run a script, click the `Run` button in the toolbar of the Python editor:

![Run a script in openLCA](run_script.png)

---

## Hello world!

You can write normal Python code in the editor. Let’s start with a simple example:

```python
print("Hello world!")
```

When you run this, the openLCA console will show:

```
Hello world!
```

![Hello world!](hello.png)

---

## Relation to standard Python

Jython supports most of the Python 2.7 standard library.

For example, this script writes a small CSV file (change the file path to a real location on your
computer):

```python
import csv

# Change this path to your own CSV file location
FILE = "~/path/to/file.csv"

data = [
    ["Tea", "1.0"],
    ["Coffee", "2.0"],
]

with open(FILE, "w") as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)
```

### Important note

Some Python libraries do **not** work with Jython:

- Libraries that use C extensions (for example NumPy)
- Parts of the standard library that Jython does not support

If you want to use normal Python (CPython) with tools like Pandas or NumPy and still connect to
openLCA, you can use the [openLCA IPC Python API](https://greendelta.github.io/openLCA-ApiDoc/).

---

## The openLCA API

With Jython, you can directly use the openLCA Java API.

You work with Java classes almost like Python classes. The main classes describe the data model, for
example:

- `Flow`
- `Process`
- `ProductSystem`

You can find these classes in the
[olca-module repository](https://github.com/GreenDelta/olca-modules/tree/master/olca-core/src/main/java/org/openlca/core/model).
