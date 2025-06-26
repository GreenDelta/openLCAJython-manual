# The db object

By default, a variable named `db` is automatically available for use when opening the Python editor.
This variable is of type `Db` and represents the openLCA database. You can use the database in the
following way:

- `db.get(modelType, id)` gets an object of type `modelType` from the database
- `db.getAll(modelType)` gets all objects of type `modelType` from the database
- `db.getForName(modelType, name)` gets the arbitrary first object of type `modelType` with name
  `name`
- `db.getDescriptor(modelType, id)` gets a descriptor of type `modelType` (useful for heavy
  datasets)
- `db.getDescriptors(modelType)` gets all descriptors of type `modelType`
- `db.insert(object)` inserts the object into the database
- `db.delete(object)` deletes the object from the database
- `db.update(object)` updates the object in the database

## Some basic examples

```python
# get the mass flow property
mass = db.get(FlowProperty, 'Mass')

# insert a newly created process
process = Process.of('Aluminium smelting', mass)
db.insert(process)

process.description = 'Process for smelting aluminium'
# update the process
db.update(process)

# delete the process
db.delete(process)
```

## More functionalities with DAO

`db` has its own limits when it comes to getting datasets with a specific name. To get a list of the
datasets with a specific name, you can use the model DAO. Each model has its own model DAO:
`ProcessDao`, `FlowDao`, `ProductSystemDao`, etc.

DAO can be used with the following methods:

- `ModelDao(db).getForName(name)` gets all the datasets with the name `name`
- `ModelDao(db).getAll()` gets all the datasets
- `ModelDao(db).deleteAll()` deletes all the datasets (use with caution)

For example, to get all the processes with the name `Aluminium smelting`:

```python
processes = ProcessDao(db).getForName('Aluminium smelting')
```
