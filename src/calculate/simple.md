# Run a calculation

```python
# retrieve an existing product system from the database
system = db.get(ProductSystem, "UUID_of_the_product_system")

# retrieve the impact method
method = db.get(ImpactMethod, "UUID_of_the_impact_method")

# create the calculation setup
setup = CalculationSetup.of(system).withImpactMethod(method)
# run the calculation
result = SystemCalculator(db).calculate(setup)

# get the total impact value for the first impact category
impact = next(cat for cat in method.impactCategories)
value = result.getTotalImpactValueOf(Descriptor.of(impact))
print(
    "The total impact on %s for %s is %.3f %s."
    % (impact.name, system.name, value, impact.referenceUnit))
```

```python
# Output:
#  The total impact on Water use for Coffee brewing is 0.004 m3.
```
