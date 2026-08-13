# Update a process (edit, add information, etc.)

```python
# let's say, we have created an inserted a process
mass = db.getForName(FlowProperty, "Mass")
aluminium_ingot = Flow.product("Aluminium ingot", mass)
aluminium_production = Process.of("Aluminium production", aluminium_ingot)
# get the process UUID to retrieve it from the database
uuid = aluminium_production.refId
db.insert(aluminium_ingot, aluminium_production)

# get the process from the database (UUID can be copied from the process page)
process = db.get(Process, uuid)

# add more information to the process dataset
process.description = "The process of aluminium production"
process.defaultAllocationMethod = AllocationMethod.PHYSICAL
process.infrastructureProcess = False
germany = db.getForName(Location, "Germany")
process.location = germany

# increase the version and update the last update date
Version.incUpdate(process)  # incMinor/incMajor to increase minor/major version
# update the process in the database
db.update(process)

# refresh the navigator to see the new process
App.runInUI("Refresh navigator", lambda: Navigator.refresh())
```
