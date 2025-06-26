# Cheat sheet

## Delete a line

To delete a line in the Python editor, place the cursor on the line you want to delete and press
`Ctrl+X`.

## Clear the console

You can clear the console before running the code with the following command:

```python
from org.eclipse.ui.console import ConsolePlugin

consoles = ConsolePlugin.getDefault().getConsoleManager().getConsoles()
console = next(c for c in consoles if c.getName() == "openLCA")
console.clearConsole()
```

You can add this [script](console.py) to your own directory (e.g.
`~/openLCA-data-1.4/python/utils.py`) and run it with the following command:

```python
from utils import Console

Console.clear()
```
