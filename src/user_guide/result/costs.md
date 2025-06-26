# Costs

The LCC (Life Cycle Costing) results are only available if the system has been calculated with the
`withCosts(True)` method applied.

## Life cycle costing result

To get the life cycle costing results, we use the `getTotalCosts` method. It will return the total
cost of the system as a float.

```python
currency = system.referenceExchange.currency.name
total_cost = result.getTotalCosts()
print("The total cost of the system is %s %s." % (total_cost, currency))
```

## Direct contributions

Similar to the direct contributions of the inventory, we can get the direct contributions of a
process to the life cycle cost of the system with the `getDirectCostValues` method. It will return a
list of `TechFlowValue`. For example:

```python
contributions = result.getDirectCostValues()
for contribution in contributions:
    print(
        "The contribution of %s in %s is %s %s."
        % (
            contribution.techFlow().flow().name,
            contribution.techFlow().provider().name,
            contribution.value(),
            currency,
        )
    )
```

## Total values

Similar to the total values of the inventory, we can get the total costs of a process at a point in
the supply chain. It will take into account the direct, upstream and downstream costs.

```python
total_costs = result.getTotalCostValues()
for total_cost in total_costs:
    print(
        "The total cost of %s in %s is %s %s."
        % (
            total_cost.flow().name,
            total_cost.provider().name,
            total_cost.value(),
            currency,
        )
    )
```
