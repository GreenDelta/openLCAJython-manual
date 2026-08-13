# Delete a product system
```python
# let's assume we want to delete the following product system from the database
mass = db.getForName(FlowProperty, "Mass")
f = Flow.product("Flow", mass)
p = Process.of("Process", f)
s = ProductSystem.of("Product system", p)
uuid = s.refId
db.insert(f, p, s)

# get the product system from the database
product_system = db.get(ProductSystem, uuid)

# delete the product system from the database
db.delete(product_system)

# refresh the navigator
App.runInUI("Refresh navigator", lambda: Navigator.refresh())
```
