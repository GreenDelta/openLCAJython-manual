# Create a flow from scratch

The following example creates three flows: a **product**, a **waste** and an **elementary** flow.

Each flow created in openLCA must be associated with a reference flow property, such as mass, volume,
area, and so on — this is the second argument passed to `Flow.product`, `Flow.waste` and
`Flow.elementary` below.

```python
# get the mass and volume flow properties from the database
mass = db.getForName(FlowProperty, "Mass")
volume = db.getForName(FlowProperty, "Volume")

# create a product flow
aluminium_ingot = Flow.product("Aluminium ingot", mass)

# create a waste flow
waste_water = Flow.waste("Industrial waste water", volume)

# create an elementary flow
water = Flow.elementary("Water", volume)

# insert the flows into the database
db.insert(aluminium_ingot, waste_water, water)

# refresh the navigator to see the new flows
App.runInUI("Refresh navigator", lambda: Navigator.refresh())
```
