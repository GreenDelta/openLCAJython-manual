# Running SQL queries

You can run SQL queries on the database using the `NativeSql` class. You will need to create a
handler function to collect the results that return `True` to continue the query, or `False` to stop
it.

For example to collect all the processes that have Trichlorofluoromethane as output:

```python
flows = FlowDao(db).getForName('Trichlorofluoromethane')
processes = []  # List[str]

def collect_results(record):
    process = db.get(Process, record.getLong(1))
    processes.append(process.name)
    return True

for flow in flows:
    query = (
        "SELECT f_owner FROM tbl_exchanges WHERE f_flow = %i AND is_input = 0"
        % flow.id
    )
    NativeSql.on(db).query(query, collect_results)

print("\n".join(processes))
```
