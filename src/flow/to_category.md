# Move a flow to a category

```python
# create only categories that do not exist, the path is provided
flow_category = CategoryDao.sync(db, ModelType.FLOW, "Material", "Metal")

# creates a product flow and add its category
mass = db.getForName(FlowProperty, "Mass")
product = Flow.product("Gold", mass)
product.category = flow_category

db.insert(product)

# refresh the navigator
App.runInUI("Refresh navigator", lambda: Navigator.refresh())
```
