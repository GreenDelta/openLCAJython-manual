# Clear the console

```python
from org.eclipse.ui.console import ConsolePlugin

consoles = ConsolePlugin.getDefault().getConsoleManager().getConsoles()
console = next(c for c in consoles if c.getName() == "openLCA")
console.clearConsole()
```
