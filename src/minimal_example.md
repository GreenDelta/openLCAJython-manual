# A minimal example

This chapter provides a straightforward example of using the openLCA Jython interface to access
datasets and perform a calculation.

The objective is to create a basic model for boiling water and evaluate its environmental impact
using the EPD 2018 impact method. This example serves as a starting point for working with openLCA
programmatically, demonstrating how to retrieve data and run calculations efficiently.

This example assumes a database with reference data and the LCIA methods, open in openLCA. If you do
not have one yet, see [Set up a database](set_up_a_database.md).

Now that you have created a database and opened it, you will be able to interact with its datasets
via the Python script. The routine is quite simple: create datasets and add them to the database
(`db.insert`) or retrieve them from the database (`db.getForName` or `db.get`).

```python
## Create the product system

# First, let's create a flow representing Boiling water, using a Volume as
# dimension. The `FlowProperty` tells the system how to measure the quantity
# of this flow – i.e. in any unit of volume (liters or cubic meters, ... ).

# retrieve the flow property from the database
volume = db.getForName(FlowProperty, "Volume")
assert isinstance(volume, FlowProperty), "Volume flow property not found"
# create the flow with its name and flow property
boiling_water = Flow.product("Boiling water", volume)

# create a process for boiling water (name and reference flow)
boiling_water_kettle = Process.of(
    "Boiling water with an electric kettle", boiling_water
)

# retrieve the water flow from the database
water = db.getForName(Flow, "Water")
assert isinstance(water, Flow), "Water flow not found"
# add the water flow to the process as an input
boiling_water_kettle.input(water, 0.001)  # m3

# create a flow for the electricity needed for the kettle
# retrieve the energy flow property from the database
energy = db.getForName(FlowProperty, "Energy")
assert isinstance(energy, FlowProperty), "Energy flow property not found"
# create the flow for the electricity
electricity = Flow.product("Electricity", energy)
# add the electricity flow to the process
boiling_water_kettle.input(electricity, 0.35)  # MJ

# create a process for the electricity production
electricity_production = Process.of("Electricity production", electricity)
# get the flow for coal
coal = db.getForName(Flow, "Coal, hard, unspecified")
assert isinstance(coal, Flow), "Coal flow not found"
# add the coal flow to the process
electricity_production.input(coal, 0.05)  # kg

# insert the flows and processes into the database
db.insert(boiling_water, electricity, boiling_water_kettle, electricity_production)

# It is important to insert the processes and the flows before running the
# `ProductSystem.link` method. If you run the `ProductSystem.link` method before
# inserting the processes and the flows, openLCA won't be able to correctly
# link the processes.

# create a product system
system = ProductSystem.of("Boiling water with an electric kettle", boiling_water_kettle)
# link the processes to the exchanges
system.link(electricity_production, boiling_water_kettle)

# the product system only exists in memory, so we need to insert the product
# system in the database
db.insert(system)

# refresh the navigator to see the new processes, flows and product system
App.runInUI("Refresh navigator", lambda: Navigator.refresh())


## Run a calculation

# To run a calculation, we need to create a calculation setup with the product
# system that we have created as well as the _EPD 2018_ impact method. The
# calculation is then run with the `SystemCalculator` class.

# retrieve the EPD 2018 impact method
method = db.getForName(ImpactMethod, "EPD 2018")
# create the calculation setup
setup = CalculationSetup.of(system).withImpactMethod(method)
# run the calculation
result = SystemCalculator(db).calculate(setup)

# Now that the calculation has run, we can access the results. For example, we
# can get the total impact value of the _Abiotic depletion, fossil fuels_
# impact category (as an example).

# retrieve the Abiotic depletion, fossil fuels impact category
categories = list(method.impactCategories)
# searching in the list of impact categories
impact = next(i for i in categories if i.name == "Abiotic depletion, fossil fuels")
# get the total impact value for the impact
value = result.getTotalImpactValueOf(Descriptor.of(impact))

print(
    "The total impact on %s for %s is %.3f %s."
    % (impact.name, system.name, value, impact.referenceUnit)
)

# Output:
#   The total impact on Abiotic depletion, fossil fuels for Boiling water with
#   an electric kettle is 0.318 MJ.
```
