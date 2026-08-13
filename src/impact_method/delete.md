# Delete an impact method
```python
# let's assume we want to delete the following impact method from the database
method = ImpactMethod.of("Impact method")
uuid = method.refId
db.insert(method)

# get the impact method from the database
impact_method = db.get(ImpactMethod, uuid)

# delete the impact method from the database
db.delete(impact_method)

# refresh the navigator
App.runInUI("Refresh navigator", lambda: Navigator.refresh())
```
