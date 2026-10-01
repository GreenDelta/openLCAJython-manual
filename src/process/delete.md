# Delete a process

Remove a process from the database by fetching it and passing it to `db.delete`.

```python
# let's assume we want to delete the following process from the database
mass = db.getForName(FlowProperty, "Mass")
f = Flow.product("Flow", mass)
p = Process.of("Process", f)
uuid = p.refId
db.insert(f, p)

# get the process from the database
process = db.get(Process, uuid)

# delete the process from the database
db.delete(process)

# refresh the navigator
App.runInUI("Refresh navigator", lambda: Navigator.refresh())
```
