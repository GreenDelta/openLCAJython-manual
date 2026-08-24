# Impact categories

## Impact assessment result

In order to get the results of an impact assessment, we use the `getTotalImpacts` method. It will
return a list of `ImpactValue`s. An `ImpactValue` provides two methods: `impact()` that describes
the impact category and `value()`.

> **_NOTE:_** More information about `ImpactDescriptor` can be found in the
> [Meta classes](../../advanced/meta_classes.md#impactdescriptor) chapter.

```python
impacts = result.getTotalImpacts()
for impact in impacts:
    print(
        "The total impact on %s is %s %s."
        % (
            impact.impact().name,
            impact.value(),
            impact.impact().referenceUnit,
        )
    )
```

## Normalized impact assessment result

In order to get the normalized results of an impact assessment, we use the `normalize` method of the
`NwSetTable`:

```python
impacts = result.getTotalImpacts()

# retrieve the normalization and weighting set table
assert setup.nwSet() is not None
factors = NwSetTable.of(db, setup.nwSet())

# calculate the normalized impacts
normalized_impacts = factors.normalize(impacts)

for impact in normalized_impacts:
    print(
        "The normalized impact on %s is %s."
        % (
            impact.impact().name,
            impact.value(),
        )
    )
```

## Weighted impact assessment result

In order to get the weighted results of an impact assessment, we use the `weight` method of the
`NwSetTable`:

```python
impacts = result.getTotalImpacts()

# retrieve the normalization and weighting set
assert setup.nwSet() is not None
factors = NwSetTable.of(db, setup.nwSet())

# calculate the weighted impacts
weighted_impact_values = factors.weight(impacts)
for impact in weighted_impact_values:
    print(
        "The weighted impact on %s is %s."
        % (
            impact.impact().name,
            impact.value(),
        )
    )
```

## Direct contributions

To get the direct contributions of a each process to the impact result of an impact category, we use
the `getDirectImpactValuesOf` method. It will return a list of `TechFlowValue`.

```python
# retrieve the first impact category
category = method.impactCategories[0]
contributions = result.getDirectImpactValuesOf(Descriptor.of(category))
for contribution in contributions:
    print(
        "The contribution of %s in %s is %s ."
        % (
            contribution.techFlow().flow().name,
            contribution.techFlow().provider().name,
            contribution.value(),
        )
    )
```

## Direct process results

The direct process results are the direct impacts of a process in the calculated product system. We
use the `getDirectImpactsOf` method. It will return a list of `ImpactValue`s.

```python
tech_index = result.techIndex()
# loop over the technosphere flows
for tech_flow in tech_index:
    print(
        "Provider[%s] Flow[%s]" % (tech_flow.provider().name, tech_flow.flow().name)
    )
    impacts = result.getDirectImpactsOf(tech_flow)
    for impact in impacts:
        print(
            "  The direct impact on %s is %s %s."
            % (
                impact.impact().name,
                impact.value(),
                impact.impact().referenceUnit,
            )
        )
```

## Total process results

The total process results are the total impacts of a process in the calculated product system at the
stage of the supply chain. It takes into account the direct, upstream, and downstream impacts. We
use the `getTotalImpactsOf` method. It will return a list of `ImpactValue`s.

```python
tech_index = result.techIndex()
for tech_flow in tech_index:
    print(
        "Provider[%s] Flow[%s]" % (tech_flow.provider().name, tech_flow.flow().name)
    )
    impacts = result.getTotalImpactsOf(tech_flow)
    for impact in impacts:
        print(
            "  The total impact on %s is %s %s."
            % (
                impact.impact().name,
                impact.value(),
                impact.impact().referenceUnit,
            )
        )
```
