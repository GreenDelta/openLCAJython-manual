# Get impact method from the database

```python
# get and print the impact method by name
impact_method_by_name = db.getForName(ImpactMethod, "AWARE")
print(impact_method_by_name)

# get and print the impact method by id (copy the UUID from the openLCA impact method page)
impact_method_by_id = db.get(ImpactMethod, "UUID_of_the_impact_method")
print(impact_method_by_id)

# get and print the descriptor of a impact method (smaller object)
impact_method = db.getDescriptor(ImpactMethod, "UUID_of_the_impact_method")
print(impact_method)

# get and print all the database impact methods (can take a while)
impact_methods = db.getAll(ImpactMethod)
for impact_method in impact_methods:
    print(impact_method)

# get and print all the database impact method descriptors (can take a while)
impact_method_descriptors = db.getDescriptors(ImpactMethod)
for impact_method_descriptor in impact_method_descriptors:
    print(impact_method_descriptor)
```
