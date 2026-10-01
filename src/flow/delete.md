# Delete a flow

Remove a flow from the database by fetching it and passing it to `db.delete`.

```python
# let's assume we want to delete the following flow from the database
mass = db.getForName(FlowProperty, "Mass")
f = Flow.product("Flow", mass)
uuid = f.refId
db.insert(f)

# get the flow from the database
flow = db.get(Flow, uuid)

# delete the flow from the database
db.delete(flow)

# refresh the navigator
App.runInUI("Refresh navigator", lambda: Navigator.refresh())
```
