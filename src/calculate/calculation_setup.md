# Extended calculation setup

The calculation setup can be configured by adding the `with...` methods.

## Allocation method

The allocation method can be selected among the following options:
- `AllocationMethod.USE_DEFAULT`,
- `AllocationMethod.CAUSAL`,
- `AllocationMethod.ECONOMIC`,
- `AllocationMethod.NONE`,
- `AllocationMethod.PHYSICAL`

The default allocation method is `AllocationMethod.USE_DEFAULT`. To use a different allocation
method, you can use the `withAllocationMethod` method:

```python
# retrieve an existing product system and method from the database
system = db.get(ProductSystem, "UUID_of_the_product_system")
method = db.getForName(ImpactMethod, "AWARE")

# create the calculation setup with the economic allocation method
setup = (
    CalculationSetup.of(system)
        .withImpactMethod(method)
        .withAllocationMethod(AllocationMethod.ECONOMIC)
)

result = SystemCalculator(db).calculate(setup)
```


## Costs

When running an LCC (Life Cycle Costing) calculation on a product system with costs, the costs can
be included in the calculation with the `withCosts` method:

```python
# retrieve an existing product system and method from the database
system = db.get(ProductSystem, "UUID_of_the_product_system")
method = db.getForName(ImpactMethod, "AWARE")

# create the calculation setup with the economic allocation method
setup = (
    CalculationSetup.of(system)
        .withImpactMethod(method)
        .withCosts(True)
)

result = SystemCalculator(db).calculate(setup)
```

## Regionalization

With openLCA you can perform regionalized impact assessment, accounting for specific conditions and
characteristics of the location where the processes occur. To enable regionalization, you can use
the `withRegionalization` method:

```python
# retrieve an existing product system and method from the database
system = db.get(ProductSystem, "UUID_of_the_product_system")
method = db.getForName(ImpactMethod, "AWARE")

# create the calculation setup with the economic allocation method
setup = (
    CalculationSetup.of(system)
        .withImpactMethod(method)
        .withRegionalization(True)
)

result = SystemCalculator(db).calculate(setup)
```
