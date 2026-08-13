# Update exchange amount

```python
# let's say we have the following process in the database
mass = db.getForName(FlowProperty, "Mass")
tomato = Flow.product("Tomato", mass)
tomato_production = Process.of("Tomato production", tomato)
db.insert(tomato, tomato_production)

# get the "Tomato production" process
process = db.get(Process, tomato_production.refId)

# get the exchange for "Tomato" by picking the first exchange with this name
tomato_exchange = next(e for e in process.exchanges if e.flow.name == "Tomato")

# update the amount
tomato_exchange.amount = 0.1
print(tomato_exchange)

# increase the version and update the last update date
Version.incUpdate(process)  # incMinor/incMajor to increase minor/major version
# update the process in the database
db.update(process)

# refresh the navigator to see the new process
App.runInUI("Refresh navigator", lambda: Navigator.refresh())
```

```python
# Output:
#  Exchange [flow=RootEntity [type=Flow, refId=<UUID>, name=Tomato], input=false,amount=0.1, unit=Unit [id=<id>, name=kg]]
```
