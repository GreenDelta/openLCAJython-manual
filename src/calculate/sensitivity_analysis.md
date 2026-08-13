# Sensitivity analysis

In this example, we will run a sensitivity analysis on the model created in
[Parameter redefinitions](parameter_redefinitions.md#create-a-parametrized-product-system-you-can-skip-this-step).

```python
# retrieve an existing product system from the database
system = db.getForName(ProductSystem, "Coffee brewing")

# retrieve the impact method
method = db.getForName(ImpactMethod, "AWARE")

# target parameters
intensity = db.getForName(Parameter, "intensity")
with_milk = db.getForName(Parameter, "with_milk")
# process (scope) of the with_milk parameter
coffee_brewing = db.getForName(Process, "Coffee brewing")

# pick the first impact category of the impact method
impact = next(cat for cat in method.impactCategories)
# r is a dictionary of the form {(intensity, with_milk): value}
r = {}
# run the analysis over a range of intensity, with (1) or without (0) milk
for m in [0, 1]:
    for i in [0, 2, 4, 6, 8, 10]:
        parameters = [
            ParameterRedef.of(intensity, i),
            ParameterRedef.of(with_milk, coffee_brewing, m),
        ]
        setup = (
            CalculationSetup.of(system)
            .withImpactMethod(method)
            .withParameters(parameters)
        )
        result = SystemCalculator(db).calculate(setup)
        value = result.getTotalImpactValueOf(Descriptor.of(impact))

        r[(i, m)] = value

# print the results
keys = sorted(r.keys())
print("%10s %10s %20s" % ("Intensity", "Milk", impact.name))
for (i, m) in keys:
    milk = "No" if m == 0 else "Yes"
    print("%10d %10s %20s" % (i, milk, r[(i, m)]))
```

```python
# Output:
#   Intensity       Milk            Water use
#           0         No             0.004295
#           0        Yes             2.151795
#           2         No             0.090195
#           2        Yes             2.237695
#           4         No             0.176095
#           4        Yes             2.323595
#           6         No             0.261995
#           6        Yes             2.409495
#           8         No             0.347895
#           8        Yes             2.495395
#          10         No             0.433795
#          10        Yes             2.581295
```
