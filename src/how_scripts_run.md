# Technical details

Scripts run in the editor at `Tools → Developer Tools → Python`, using Jython (Python 2.7). The editor
prepares the environment so that the openLCA data model and the current database are available without
any setup on your part.

## You don't need to import openLCA classes

openLCA's data model and tools are made available automatically, so you can use them directly, without
any `import`. That is why the examples in this manual have no import lines for them.

The ones you will meet first are `Flow`, `Process`, `ProductSystem` and `ImpactMethod` for the data, and
`CalculationSetup` and `SystemCalculator` for running a calculation.

Many more are available. For the complete list — and how to look up what each class can do — see
[Available classes and imports](advanced/imports.md).

## The `db` variable is your database

The open database is always available as the variable `db`. Use it to read and write datasets:

- `db.get(Flow, uuid)` — get one dataset by its UUID
- `db.getForName(Flow, "Water")` — get one dataset by name
- `db.getAll(Flow)` — get every dataset of a type
- `db.insert(entity)`, `db.update(entity)`, `db.delete(entity)` — save your changes

`db` is `None` when no database is open, so open one first — see
[Set up a database](set_up_a_database.md).

Two more variables are always available: `log`, for writing messages to the log, and `direct`, a helper
for the occasional lazy collection field.

## Standard Python, and its limits

Jython is an implementation of Python 2.7 and supports most of its standard library, so ordinary Python
works as expected — reading and writing files, string formatting, the `csv` module, and so on.

One thing to watch: this is Python **2.7**, not Python 3, so a few conveniences you may expect are
missing or behave differently — there are no f-strings (use `"total: %s" % value` or
`"total: {}".format(value)`), dividing two integers truncates (`1 / 2` is `0`, not `0.5`), and text and
encoding are handled differently. The [Python 2.7 documentation](https://docs.python.org/2.7/) is the
reference for these.

The other limitation is that libraries relying on C extensions, such as NumPy and Pandas, are not
available. If your work depends on those, you can control openLCA from your own Python installation
using the [IPC API](https://greendelta.github.io/openLCA-ApiDoc/).
