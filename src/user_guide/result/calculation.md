# Calculation and results

After you've completed the modeling of your processes, created your product system, it's time to run
a calculation.

For demonstration purposes, we create a calculation setup for a
[product system of an _ecoinvent_ process](../data_model/product_system.md) and run it.

## Getting an impact method

The impact method can be retrieved from the database using the `db.getForName` method:

```python
method = db.getForName(ImpactMethod, "EF v3.1")
```

## Running a calculation

The calculation of a product system is done by creating a calculation setup and running the
`calculate` method of the `SystemCalculator`. The calculation setup is an object that contains all
the information needed for the calculation:

- the target product system or process,
- the amount of the functional unit,
- the LCIA method,
- the normalization and weighting sets,
- the parameter redefinitions,
- the allocation method,
- with or without costs,
- with and without regionalization,
- ...

```python
setup = CalculationSetup.of(system).withAmount(4.2).withImpactMethod(method)

result = SystemCalculator(db).calculate(setup)

for impact in result.getTotalImpacts():
    print(
        "%s: %.3f %s"
        % (impact.impact().name, impact.value(), impact.impact().referenceUnit)
    )
```

## `LcaResult` object

The result of the calculation is a `LcaResult` object. It provides an interface for accessing impact
factors, total flows, and contributions and many other objects in a structured way. The manual won't
cover all the accessible methods of the `LcaResult` object. For more information, please refer to
the
[class](https://github.com/GreenDelta/olca-modules/blob/master/olca-core/src/main/java/org/openlca/core/results/LcaResult.java#L82)
itself.

For the following examples, let's assume we have calculated the results of a product system under
the Python variable `result`.

## Specific setup options

### Normalization and weighting set

The `withNwSet` method allows to specify a normalization and weighting set. The normalization and
weighting set can be retrieved from the database by using the `ImpactMethod` object:

```python
nw_sets = method.nwSets
nw_set = next(
    nw_sets for nw_sets in nw_sets if nw_sets.name == "EF v3.1 | Global Reference 2010"
)
setup.withNwSet(nw_set)
```

### Parameter redefinitions

The parameters of a product system can be redefined using the `withParameters` method. For example,
you can replace the value of a global input parameter with a new value:

```python
g = db.getForName(Parameter, "g")
parameters = [ParameterRedef.of(g, 1.62)]
setup.withParameters(parameters)
```

### Parameter redefinition set

You can select one of the product system parameter redefinition sets to use with the in the
calculation setup:

```python
assert "Scenario 1" in [p.name for p in system.parameterSets]
setup.withParameterSetName("Scenario 1")
```

### Allocation method

The allocation method can be selected among the following options:

```python
class AllocationMethod:
    USE_DEFAULT,
    CAUSAL,
    ECONOMIC,
    NONE,
    PHYSICAL,
```

The default allocation method is `AllocationMethod.USE_DEFAULT`. To use a different allocation
method, you can use the `withAllocationMethod` method:

```python
setup.withAllocationMethod(AllocationMethod.CAUSAL)
```

### Other options

#### With or without costs

When running an LCC (Life Cycle Costing) calculation on a product system with costs, the costs can
be included in the calculation with the `withCosts` method:

```python
setup.withCosts(True)  # default is False
```

#### With or without regionalization

With openLCA you can perform regionalized impact assessment, accounting for specific conditions and
characteristics of the location where the processes occur. To enable regionalization, you can use
the `withRegionalization` method:

```python
setup.withRegionalization(True)  # default is False
```
