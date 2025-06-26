# Impact categories

## Impact assessment result

In order to get the results of an impact assessment, we use the `getTotalImpacts` method. It will
return a list of `ImpactValue`s.

```python
class ImpactValue:
  def impact(): # () -> ImpactDescriptor
  def value(): # () -> float
```

> **_NOTE:_** More information about `ImpactDescriptor` can be found in the
> [The advanced data model](../data_model/advanced_data_model.md#rootdescriptors) chapter.

```python
impact_values = result.getTotalImpacts()
for impact_value in impact_values:
    print(
        "The total impact on %s is %s %s."
        % (
            impact_value.impact().name,
            impact_value.value(),
            impact_value.impact().referenceUnit,
        )
    )
```

## Normalized impact assessment result

In order to get the normalized results of an impact assessment, we use the `normalize` method of the
`NwSetTable`:

```python
impact_values = result.getTotalImpacts()
assert setup.nwSet() is not None
factors = NwSetTable.of(db, setup.nwSet())
normalized_impact_values = factors.normalize(impact_values)
for impact_value in normalized_impact_values:
    print(
        "The normalized impact on %s is %s."
        % (
            impact_value.impact().name,
            impact_value.value(),
        )
    )
```

## Weighted impact assessment result (TODO)

In order to get the weighted results of an impact assessment, we use the `apply` method of the
`NwSetTable`:

```python
impact_values = result.getTotalImpacts()
assert setup.nwSet() is not None
factors = NwSetTable.of(db, setup.nwSet())
weighted_impact_values = factors.apply(impact_values)
for impact_value in weighted_impact_values:
    print(
        "The weighted impact on %s is %s."
        % (
            impact_value.impact().name,
            impact_value.value(),
        )
    )
```

## Direct contributions

To get the direct contributions of a each process to the impact result of an impact category, we use
the `getDirectImpactValuesOf` method. It will return a list of `TechFlowValue`.

```python
climate_change = next(c for c in method.impactCategories if c.name == "Climate change")
contributions = result.getDirectImpactValuesOf(Descriptor.of(climate_change))
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
impacts = result.getDirectImpactsOf(tech_flow)
for impact in impacts:
    print(
        "The direct impact on %s is %s %s."
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
impacts = result.getTotalImpactsOf(tech_flow)
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
