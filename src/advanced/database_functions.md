# More database functions

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
