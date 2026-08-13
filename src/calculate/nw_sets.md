# Normalization and weighting sets

The `withNwSet` method allows to specify a normalization and weighting set. The normalization and
weighting set can be retrieved from the impact method.

```python
# retrieve an existing product system from the database
system = db.get(ProductSystem, "UUID_of_the_product_system")

# retrieve the impact method
method = db.getForName(ImpactMethod, "EF 3.1 Method (adapted)")

# retrieve the normalization and weighting set
nw_sets = method.nwSets
nw_set = next(
    nw_sets for nw_sets in nw_sets if nw_sets.name == "EF 3.1 normalization and weighting set"
)

setup = (
    CalculationSetup.of(system)
        .withImpactMethod(method)
        .withNwSet(nw_set)
)

result = SystemCalculator(db).calculate(setup)

# get the normalized impact value for Water use
impacts = result.getTotalImpacts()
factors = NwSetTable.of(db, nw_set)
normalized_impacts = factors.normalize(impacts)
weighted_impacts = factors.weight(impacts)
normalized_impact = next(i for i in normalized_impacts if i.impact().name == "Water use")
weighted_impact = next(i for i in weighted_impacts if i.impact().name == "Water use")
print(
    "The normalized impact on %s for %s is %.6f."
    % (normalized_impact.impact().name, system.name, normalized_impact.value())
)
print(
    "The weighted impact on %s for %s is %.6f."
    % (weighted_impact.impact().name, system.name, weighted_impact.value())
)
```
