# Update an existing product system (edit, add information, etc.)

```python
# let's say, a product system has been created and inserted in the database
mass = db.getForName(FlowProperty, "Mass")
aluminium = Flow.product("Aluminium ingot", mass)
process = Process.of("Aluminium production", aluminium)
product_system = ProductSystem.of("Aluminium production", process)
# get the product system UUID to retrieve it from the database
uuid = product_system.refId
db.insert(aluminium, process, product_system)

# get the product system from the database (the UUID can be copied from the 
# product system page)
product_system = db.get(ProductSystem, uuid)

# add more information to the product system
product_system.description = "The process of aluminium production"
product_system.targetAmount = 42.0
# change the target unit from kg to g
# get unit from the flow property list of units
g = next(u for u in mass.unitGroup.units if u.name == "g")
product_system.targetUnit = g
product_system.cutoff = 12.3

# increase the version and update the last update date
Version.incUpdate(product_system)  # or incMinor/incMajor
# update the product system in the database
db.update(product_system)

# refresh the navigator to see the new product system
App.runInUI("Refresh navigator", lambda: Navigator.refresh())
```
