# Add a parameter redefinition set

```python
# create a parametrized product system

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

# create parameter redefinition sets

scenario_1 = ParameterRedefSet.of("Scenario 1", [
    ParameterRedef.of(intensity, 2),
    ParameterRedef.of(with_milk, coffee_brewing, 1.0),
])
scenario_2 = ParameterRedefSet.of("Scenario 2", [
    ParameterRedef.of(intensity, 8),
    ParameterRedef.of(with_milk, coffee_brewing, 0.0),
])

# add the parameter redefinition sets to the product system
system.parameterSets.add(scenario_1)
system.parameterSets.add(scenario_2)

# insert the product system in the database
db.insert(system)

# refresh the navigator to see the new process
App.runInUI("Refresh navigator", lambda: Navigator.refresh())
```
