# Create a process

The following example creates a process for the production of aluminium.

Inputs:

- 1.9 kg of alumina
- 0.4 kg of carbon anode
- 50.0 MJ of electricity

Outputs:

- 1.0 kg of aluminium
- 0.02 m³ of wastewater

```python
# get flow properties from the database
mass = db.getForName(FlowProperty, "Mass")
energy = db.getForName(FlowProperty, "Energy")
volume = db.getForName(FlowProperty, "Volume")

# create the product output flow (quantitative reference)
aluminium = Flow.product("Aluminium ingot", mass)

# create the aluminium production process with 1 kg of aluminium as
# quantitative reference
process = Process.of("Aluminium production", aluminium)

# add the material input flows
alumina = Flow.product("Alumina", mass)
process.input(alumina, 1.9)  # kg alumina per kg aluminium
carbon_anode = Flow.product("Carbon anode", mass)
process.input(carbon_anode, 0.4)  # kg anode consumption

# add the electricity input flow
electricity = Flow.product("Electricity, medium voltage", energy)
process.input(electricity, 50.0)  # MJ

# add waste water output flow
wastewater = Flow.waste("Industrial wastewater", volume)
process.output(wastewater, 0.02)  # m3

# insert all new objects into the database
db.insert(
    alumina,
    carbon_anode,
    electricity,
    wastewater,
    aluminium,
    process,
)

# refresh the navigator to display the new process
App.runInUI("Refresh navigator", lambda: Navigator.refresh())
```
