# Get product systems from the database

```python
# get and print the product system by name
product_system_by_name = db.getForName(ProductSystem, "Aluminium ingot")
print(product_system_by_name)

# get and print the product system by id (copy the UUID from the openLCA product system page)
product_system_by_id = db.get(ProductSystem, "UUID_of_the_product_system")
print(product_system_by_id)

# get and print the descriptor of a product system (smaller object)
product_system = db.getDescriptor(ProductSystem, "UUID_of_the_product_system")
print(product_system)

# get and print all the database product systems (can take a while)
product_systems = db.getAll(ProductSystem)
for product_system in product_systems:
    print(product_system)

# get and print all the database product system descriptors (can take a while)
product_system_descriptors = db.getDescriptors(ProductSystem)
for product_system_descriptor in product_system_descriptors:
    print(product_system_descriptor)
```
