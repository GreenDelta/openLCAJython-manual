# A minimal example

This chapter provides a straightforward example of using the openLCA Jython interface to access
datasets and perform a calculation.

The objective is to create a basic model for boiling water and evaluate its environmental impact
using the EPD 2018 impact method. This example serves as a starting point for working with openLCA
programmatically, demonstrating how to retrieve data and run calculations efficiently.

## Create an empty database with reference data and LCIA methods

In the menu, click on `Database → New database → From scratch...`, input a database name and select
_Complete reference data_ before clicking on _Finish_.

This will create an empty database with the reference data. For more information, see
[Creating a new database from scratch](https://greendelta.github.io/openLCA2-manual/databases/create_database.html#creating-a-new-database-from-scratch).

Once the database is created, download the openLCA LCIA methods package from Nexus and import it
into the database you have created. For more information, see
[Importing LCIA methods into openLCA](https://greendelta.github.io/openLCA2-manual/lcia_methods/importing_lcia_methods.html).

This database is often a good starting point to start modeling with the Python interface (and in
openLCA more generally).

## Create the product system from scratch

Now that you have created a database and opened it, you will be able to interact with its datasets
via the Python script. The routine is quite simple: create datasets and add them to the database
(`db.insert`) or retrieve them from the database (`db.getForName` or `db.get`).

> **_NOTE:_** You can run the following lines of code by copy-pasting them in the openLCA Python
> console. You can also copy the whole [script](minimal_example.py).

First, let's create a flow representing _Boiling water_, using a _Volume_ as dimension. The
`FlowProperty` tells the system how to measure the quantity of this flow–i.e. in any unit of volume
(liters or cubic meters, ... ).

```python
volume = db.getForName(FlowProperty, "Volume")
boiling_water = Flow.product("Boiling water", volume)
```

In the first line, the flow property for volumes is retrieved from the database (more details about
it in [The basic data model](../user_guide/data_model/basic_data_model.md) chapter). In the second
line, the product flow is created with its name and its flow property.

It is now time to create the process for boiling water with an electric kettle. Let's create a
process with its name and its reference flow.

```python
boiling_water_kettle = Process.of(
    "Boiling water with an electric kettle", boiling_water
)
```

Let's now add inputs to the process. First, we can retrieve the _Water_ elementary flow from the
reference data. Second, we create a flow for the electricity needed for the kettle and add it to the
process.

```python
water = db.getForName(Flow, "Water")
boiling_water_kettle.input(water, 0.001)  # m3

energy = db.getForName(FlowProperty, "Energy")
electricity = Flow.product("Electricity", energy)
boiling_water_kettle.input(electricity, 0.35)  # MJ
```

The next step is to create a process for the electricity production. We will call it _Electricity
production_ and make it really simple for the sake of the example.

```python
electricity_production = Process.of("Electricity production", electricity)
coal = db.getForName(Flow, "Coal, hard, unspecified")
electricity_production.input(coal, 0.05)  # kg
```

Now that all the elements needed to build the product system are created, it is time to insert them
in the database.

```python
db.insert(boiling_water, electricity, boiling_water_kettle, electricity_production)
```

We can now create the product system. Now that it is important to insert the processes and the flows
before running the `ProductSystem.link` method. If you run the `ProductSystem.link` method before
inserting the processes and the flows, openLCA won't be able to correctly link the processes.

```python
system = ProductSystem.of("Boiling water with an electric kettle", boiling_water_kettle)
system.link(coal, boiling_water_kettle)
db.insert(system)
```

After the two first lines, the system only exist in memory. To store it in the database, we need to
run the `db.insert` method. It will also insert the processes and the flows in the database.

After running this code, refresh the navigator by clicking on the tree dot and then on _Refresh_.
The newly created flow, processes and product system should appear in their respective folder.

## Run a calculation

To run a calculation, we need to create a calculation setup with the product system that we have
created in the previous section as well as the _EPD 2018_ impact method. The calculation is then run
with the `SystemCalculator` class.

```python
method = db.getForName(ImpactMethod, "EPD 2018")
setup = CalculationSetup.of(system).withImpactMethod(method)
result = SystemCalculator(db).calculate(setup)
```

Now that the calculation has been run, we can access the results. For example, we can get the total
impact value of the _Abiotic depletion, fossil fuels_ impact category.

```python
categories = list(method.impactCategories)
impact = next(i for i in categories if i.name == "Abiotic depletion, fossil fuels")
value = result.getTotalImpactValueOf(Descriptor.of(impact))

print(
    "The total impact on %s for %s is %.3f %s."
    % (impact.name, system.name, value, impact.referenceUnit)
)

# Output:
#   The total impact on Abiotic depletion, fossil fuels for Boiling water with
#   an electric kettle is 0.318 MJ.
```

In this first section, we have seen how to create flows and processes to build a product system and
how to run a calculation. In the [following chapter](../user_guide/data_model), we will understand
the data model the relationship between flows, processes and product systems in more details.
