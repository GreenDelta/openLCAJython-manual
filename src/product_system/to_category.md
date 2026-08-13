# Move a product system to a category

```python
# create only categories that do not exist, the path is provided
product_system_category = CategoryDao.sync(
    db, ModelType.PRODUCT_SYSTEM, "2026", "March"
)

# creates a product, a process and a product system
mass = db.getForName(FlowProperty, "Mass")
product = Flow.product("Iron", mass)
process = Process.of("Iron production", product)
product_system = ProductSystem.of("Iron production", process)
product_system.category = product_system_category

# insert them in correct dependency order
db.insert(product, process, product_system)

# refresh the navigator
App.runInUI("Refresh navigator", lambda: Navigator.refresh())
```
