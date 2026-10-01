# Parameter redefinitions

## Create a parametrized product system

First, build a small product system whose exchanges reference a global parameter (`intensity`) and a
process parameter (`with_milk`).

```python
number = db.getForName(FlowProperty, "Number")
mass = db.getForName(FlowProperty, "Mass")
volume = db.getForName(FlowProperty, "Volume")

# create an output product for the process
coffee_cup = Flow.product("Cup of coffee", number)
# create a process with the "Cup of coffee" as quantitative reference
coffee_brewing = Process.of("Coffee brewing", coffee_cup)

# create the input product flows: water, coffee
coffee = Flow.product("Coffee", mass)
water = db.getForName(Flow, "Water/m3")
coffee_brewing.input(water, 0.0001)

# create the coffee exchange with a formula using a global parameter
coffee_input = Exchange.of(coffee)
# creating a global parameter for the coffee intensity
intensity = Parameter.global("intensity", 1.0)
intensity.description = "The intensity of the coffee brewing process (0-10)"
coffee_input.formula = "0.01 * " + intensity.name
# set the exchange default amount
coffee_input.amount = 0.01 * intensity.value
coffee_input.isInput = True
# add the exchange to the process
coffee_brewing.add(coffee_input)

# create a process for the production of coffee
coffee_production = Process.of("Coffee production", coffee)
coffee_production.input(water, 0.1)

# create a milk exchange with a formula using a process parameter
milk = Flow.product("Milk", mass)
milk_input = Exchange.of(milk)
# creating a process parameter for the milk amount
with_milk = Parameter.process("with_milk", 0)
with_milk.description = "A boolean parameter to indicate if milk is added"
milk_input.formula = "0.005 * " + with_milk.name
# set the exchange default amount
milk_input.amount = 0.005 * with_milk.value
milk_input.isInput = True
# add the exchange to the process
coffee_brewing.add(milk_input)
# add the process parameter to the process
coffee_brewing.parameters.add(with_milk)

# create a process for the production of milk
milk_production = Process.of("Milk production", milk)
milk_production.input(water, 10)

# insert the process and the newly created flows into the database
# note that the with_milk parameter is not inserted as it is added to the
# milk_production process
db.insert(
    coffee_cup,
    coffee,
    milk,
    intensity,
    coffee_production,
    milk_production,
    coffee_brewing
)

# create a product system
system = ProductSystem.of("Coffee brewing", coffee_brewing)
# link the processes to the exchanges
system.link(coffee_production, coffee_brewing)
system.link(milk_production, coffee_brewing)

# insert the product system in the database
db.insert(system)

# refresh the navigator to see the new process
App.runInUI("Refresh navigator", lambda: Navigator.refresh())
```

## Run the calculation with parameter redefinitions

Then calculate that system while overriding those parameters for this run with `ParameterRedef`
values.

```python
# retrieve an existing product system from the database
system = db.getForName(ProductSystem, "Coffee brewing")

# retrieve the impact method
method = db.getForName(ImpactMethod, "AWARE")

# get the intensity parameter
intensity = db.getForName(Parameter, "intensity")

# get the with_milk process parameter and the corresponding process
with_milk = db.getForName(Parameter, "with_milk")
coffee_brewing = db.getForName(Process, "Coffee brewing")

# run the calculation with the parameter redefinitions
setup = (
    CalculationSetup.of(system)
        .withImpactMethod(method)
        .withParameters([
            ParameterRedef.of(intensity, 4.2),
            ParameterRedef.of(with_milk, coffee_brewing, 1.0),
        ])
)

result = SystemCalculator(db).calculate(setup)

# get the total impact value for the first impact category
impact = next(cat for cat in method.impactCategories)
value = result.getTotalImpactValueOf(Descriptor.of(impact))
print(
    "The total impact on %s for %s is %.3f %s."
    % (impact.name, system.name, value, impact.referenceUnit)
)
```

```python
# Output:
#  The total impact on Water use for Coffee brewing is 2.332 m3.

```
