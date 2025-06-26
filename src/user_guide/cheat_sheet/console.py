from org.eclipse.ui.console import ConsolePlugin


class Console:
    @staticmethod
    def clear():
        consoles = ConsolePlugin.getDefault().getConsoleManager().getConsoles()
        console = next(c for c in consoles if c.getName() == "openLCA")
        console.clearConsole()
