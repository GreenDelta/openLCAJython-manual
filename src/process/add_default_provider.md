# Add a default provider

In openLCA, a "provider" refers to the process that supplies a specific flow (the source or origin of
a particular input or output flow). The provider information helps to establish the relationships and
dependencies between different processes and flows within the LCA model, and makes the input / output
unique. It can be overwritten in a product system, meaning that you can select a new, different
connecting process in a product system.

_Source: [openLCA 2 manual — Inputs/Outputs](https://greendelta.github.io/openLCA2-manual/processes/tab_inputs_outputs.html)_

In this example, we create a process for the production of beer and add a default provider to the
input exchange for the production of barley.

```python
from org.openlca.core.model import ProviderType

# create a process for beer production
volume = db.getForName(FlowProperty, "Volume")
beer = Flow.product("Beer", volume)
beer_production = Process.of("Beer production", beer)
water = Flow.elementary("Water", volume)
beer_production.input(water, 1.0)

# add an input for barley
mass = db.getForName(FlowProperty, "Mass")
barley = Flow.product("Barley", mass)
barley_exchange = beer_production.input(barley, 0.42)

# create a process for barley production
process = Process.of("Barley production", barley)
# insert and get the process (the provider should be in the database before
# setting it as the default provider)
db.insert(barley, process)
barley_production = db.get(Process, process.refId)

# add a default provider for barley
barley_exchange.defaultProviderId = barley_production.id
barley_exchange.defaultProviderType = ProviderType.PROCESS

# insert the process into the database
db.insert(water, beer, beer_production)

# refresh the navigator
App.runInUI("Refresh navigator", lambda: Navigator.refresh())
```
