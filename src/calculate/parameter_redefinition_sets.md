# Calculation with parameter redefinition sets

Instead of creating a new parameter redefinition set when running a calculation, you can select one
of the product system parameter redefinition sets and use it in the calculation setup.

## Create a product system with parameter redefinition sets

Copy and paste the code from
[Add a parameter redefinition set](../product_system/add_parameter_redefinition_set.md).

## Run the calculation with a parameter redefinition set

```python
# retrieve an existing product system from the database
system = db.getForName(ProductSystem, "Coffee brewing")

# retrieve the impact method
method = db.getForName(ImpactMethod, "AWARE")

# run the calculation with the parameter redefinitions set named "Scenario 1"
# retrieve the parameter redefinition set from the product system
parameter_set = next(set for set in system.parameterSets if set.name == "Scenario 1")
setup = (
    CalculationSetup.of(system)
        .withImpactMethod(method)
        .withParameterSetName(parameter_set.name)
        .withParameters(parameter_set.parameters)
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
