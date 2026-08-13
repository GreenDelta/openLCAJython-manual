# Intervention flows

The intervention flows are the flows that cross the boundary with the environment of the calculated
system (this is why the short name is `EnviFlow`).

To retrieve the intervention matrix, we use the `enviIndex` method. It will return an iterator of
`EnviFlow`s: `EnviIndex`, which maps symmetrically the rows (intervention flows) and columns
(technosphere flows). An `EnviFlow` is a record that contains a `flow()` (the descriptor of a
`Flow`), a `location()` (as a descriptor as well), and `isInput()` (a boolean that indicates whether
the flow is an input or an output).

> **_NOTE:_** More information about `LocationDescriptor` and `FlowDescriptor` can be found in the
> [Meta classes](../../advanced/meta_classes.md) chapter.

```python
envi_index = result.enviIndex()
# loop over all the intervention flows
for envi_flow in envi_index:
    print(
        "Flow[%s] Is input?[%s] Location[%s]\n"
        % (envi_flow.flow().name, envi_flow.isInput(), envi_flow.location())
    )
```

## Inventory results

To get the inventory results, the quantitative list of all the material and energy flows into and
out of the system boundary, we use the `getTotalFlows` method. It will return a list of
`EnviFlowValue`, which is a record of an `EnviFlow` (`enviFlow()`) and `value()` the amount of the
flow.

```python
envi_flow_values = result.getTotalFlows()
for envi_flow_value in envi_flow_values:
    in_or_out = "input" if envi_flow_value.isInput() else "output"
    print(
        "The total amount of the %s %s is %s."
        % (in_or_out, envi_flow_value.flow().name, envi_flow_value.value())
    )
```

## Direct contributions

To get the direct contributions of a each process to the inventory result of a flow, we use the
`getDirectFlowValuesOf` method. It will return a list of `TechFlowValue`.

```python
envi_index = result.enviIndex()
for envi_flow in envi_index:
    print(
        "Flow[%s] Is input?[%s] Location[%s]"
        % (envi_flow.flow().name, envi_flow.isInput(), envi_flow.location())
    )
    contributions = result.getDirectFlowValuesOf(envi_flow)
    for contribution in contributions:
        print(
            "  The contribution of %s is %s."
            % (contribution.techFlow().flow().name, contribution.value())
        )
```

## Total values

The total value of a flow for a given process is the total inventory result at this point of the
supply chain. It includes the direct, upstream, and downstream (related to waste treatment)
contributions.

```python
envi_index = result.enviIndex()
for envi_flow in envi_index:
    print(
        "Flow[%s] Is input?[%s] Location[%s]"
        % (envi_flow.flow().name, envi_flow.isInput(), envi_flow.location())
    )
    total_values = result.getTotalFlowValuesOf(envi_flow)
    for total_value in total_values:
        print(
            "  The total value for %s is %s."
            % (total_value.techFlow().flow().name, total_value.value())
        )
```

## Direct process results

The direct process results are the direct intervention flows of a process to fulfill the demand of
the product system.

```python
tech_index = result.techIndex()
for tech_flow in tech_index:
    print(
        "Provider[%s] Flow[%s]" % (tech_flow.provider().name, tech_flow.flow().name)
    )
    envi_flow_values = result.getDirectFlowsOf(tech_flow)
    for envi_flow_value in envi_flow_values:
        print(
            "  The direct amount of %s is %s."
            % (envi_flow_value.enviFlow().flow().name, envi_flow_value.value())
        )
```

## And more...

For more specific methods, please refer to the
[`LcaResult` class](https://github.com/GreenDelta/olca-modules/blob/892267893253306c24c601189e9da30ad4cb5edf/olca-core/src/main/java/org/openlca/core/results/LcaResult.java#L163).
