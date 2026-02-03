# Cheat sheet

## Shortcut keys

- `Ctrl + Shift + Enter`/`Ctrl + Shift + Enter` to run the code in the editor
- `Ctrl + X`/`Cmd + X` to cut a line or a selection
- `Ctrl + C`/`Cmd + C` to copy a line or a selection
- `Ctrl + V`/`Cmd + V` to paste a line or a selection
- `Ctrl + Enter`/`Cmd + Enter` to insert a new line below the current line
- `Ctrl + /`/`Cmd + /` to comment/uncomment out a line or a selection

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
