# Create a new process with already existing flow and provider

This example creates a new process for the production of tea, using the
elementary flow "Water", already existing in the database.

```python
# let's assume the "Water" elementary flow already exists
volume = db.getForName(FlowProperty, "Volume")
flow = Flow.elementary("Water", volume)
# get the flow UUID to retrieve from the database
uuid = flow.refId
db.insert(flow)

# get the flow from the database
water = db.get(Flow, uuid)

# create a quantitative reference
mass = db.getForName(FlowProperty, "Mass")
output = Flow.product("Tea", mass)

# create the process
process = Process.of("Tea production", output)

# add the elementary flow as input
process.input(water, 1.0)

# insert the process into the database
db.insert(output, process)

# refresh the navigator
App.runInUI("Refresh navigator", lambda: Navigator.refresh())
```
