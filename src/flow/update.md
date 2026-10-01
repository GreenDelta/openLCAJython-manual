# Update a flow (edit, add information, etc.)

To change a flow, fetch it from the database, edit its fields, bump its version and write it back with
`db.update`.

```python
# let's say, we have created and inserted a flow
mass = db.getForName(FlowProperty, "Mass")
aluminium_ingot = Flow.product("Aluminium ingot", mass)
# get the flow UUID to retrieve it from the database
uuid = aluminium_ingot.refId
db.insert(aluminium_ingot)

# get the flow from the database (the UUID can be copied from the flow page)
flow = db.get(Flow, uuid)

# update the flow name
flow.name = "Aluminium bar"

# update some more properties
aluminium_ingot.description = ("A piece of relatively pure material, that is "
    + "cast into a shape suitable for further processing.")
aluminium_ingot.casNumber = "1234-56-78"
aluminium_ingot.formula = "12 * 34 / 56"
aluminium_ingot.synonyms = "aluminium, aluminium ingot"
france = db.getForName(Location, "France")
aluminium_ingot.location = france

# increase the version and update the last update date
Version.incUpdate(flow)  # or incMinor/incMajor to increase minor/major version
# update the flow in the database
db.update(flow)

# refresh the navigator to see the new flow
App.runInUI("Refresh navigator", lambda: Navigator.refresh())
```
