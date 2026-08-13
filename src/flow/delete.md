# Delete a flow

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
