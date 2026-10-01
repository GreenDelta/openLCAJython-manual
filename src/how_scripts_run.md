# How scripts run

Scripts run in the editor at `Tools → Developer Tools → Python`, using Jython (Python 2.7). The editor
sets a couple of things up for you so you can start writing straight away.

## You don't need to import openLCA classes

openLCA's data model is made available automatically, so you can use `Flow`, `Process`,
`ProductSystem`, `ImpactMethod`, `CalculationSetup` and the other core classes **directly, without any
`import`**. That is why the examples in this manual have no import lines for them.

A few helpers are the exception and are imported where they are used — you will see a
`from ... import ...` line in those examples. For what is and isn't available, see
[What you can import](advanced/imports.md).

## The `db` variable is your database

The open database is always available as the variable `db`. Use it to read and write datasets:

- `db.get(Flow, uuid)` — get one dataset by its UUID
- `db.getForName(Flow, "Water")` — get one dataset by name
- `db.getAll(Flow)` — get every dataset of a type
- `db.insert(entity)`, `db.update(entity)`, `db.delete(entity)` — save your changes

`db` is `None` when no database is open, so open one first — see
[A minimal example](minimal_example.md), which also shows how to set up a database with reference data
and the LCIA methods most scripts need.

Two more variables are always available: `log`, for writing messages to the log, and `direct`, a helper
for the occasional lazy collection field.
