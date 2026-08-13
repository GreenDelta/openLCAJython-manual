# Move to a category

```python
# create only categories that do not exist
# (Material production/Metal production)
process_category = CategoryDao.sync(
    db, ModelType.PROCESS, "Material production", "Metal production"
)

# creates a process and add its category
mass = db.getForName(FlowProperty, "Mass")
product = Flow.product("Silver", mass)
process = Process.of("Silver production", product)
process.category = process_category

# insert them in correct dependency order
db.insert(product, process)

# refresh the navigator
App.runInUI("Refresh navigator", lambda: Navigator.refresh())
```
