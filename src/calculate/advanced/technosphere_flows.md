# Technosphere flows

To retrieve the technosphere matrix, use the `techIndex` method. It will return an iterator of
`TechFlow`s, namely a `TechIndex`. It maps symmetrically the rows (products or wastes) and columns
(process, product systems, ...) of the technology matrix. A `TechFlow` is a record that contains a
`provider()` (the descriptor of a `Process`) and a `flow()` (as a descriptor as well).

> **_NOTE:_** More information about `RootDescriptor` and `FlowDescriptor` can be found in the
> [Meta classes](../../advanced/meta_classes.md) chapter.

```python
tech_index = result.techIndex()
# loop over the tech flows
for tech_flow in tech_index:
    print(
        "Provider[%s] Flow: [%s]\n" % (tech_flow.provider().name, tech_flow.flow().name)
    )
```

## Total requirements

To get the total requirements of a technosphere flow, we use the `getTotalRequirementsOf` method. It
will return the total amount of the flow required by the corresponding provider.

```python
tech_index = result.techIndex()
for tech_flow in tech_index:
    print(
        "The flow %s (Provider[%s]) requires a total amount of %s\n"
        % (
            tech_flow.flow().name,
            tech_flow.provider().name,
            result.getTotalRequirementsOf(tech_flow),
        )
    )
```

## Scaled technosphere flows

The scaled technosphere flows of a process are the scaled inputs and outputs of the linked product
and waste flows of that process related to the final demand of the product system. They can be
obtained with the `getScaledTechFlowsOf` method. It will return a list of `TechFlowValue`, which is
a record that contains a `techFlow()` (see `TechFlow` above) and a `value()` (the scaled
amount of the flow).

For example, to get the scaled technosphere flows amount of the first process in the technosphere
matrix:

```python
tech_index = result.techIndex()
for tech_flow in tech_index:
    print(
        "Provider[%s] Flow[%s]" % (tech_flow.provider().name, tech_flow.flow().name)
    )
    scaled_tech_flows = result.getScaledTechFlowsOf(tech_flow)
    for tech_flow_value in scaled_tech_flows:
        print(
            "  The scaled amount of %s is %s."
            % (tech_flow_value.techFlow().flow().name, tech_flow_value.value())
        )
```

## Unscaled technosphere flows

The unscaled requirements of a process are the direct requirements of the process related to the
quantitative reference of that process without applying a scaling factor. For example, the unscaled
amount of the flows of the last column:

```python
tech_index = result.techIndex()
for tech_flow in tech_index:
    print(
        "Provider[%s] Flow[%s]" % (tech_flow.provider().name, tech_flow.flow().name)
    )
    unscaled_tech_flows = result.getUnscaledTechFlowsOf(tech_flow)
    for tech_flow_value in unscaled_tech_flows:
        print(
            "  The unscaled amount of %s is %s."
            % (tech_flow_value.techFlow().flow().name, tech_flow_value.value())
        )
```

## For more...

For more specific methods, please refer to the
[`LcaResult` class](https://github.com/GreenDelta/olca-modules/blob/892267893253306c24c601189e9da30ad4cb5edf/olca-core/src/main/java/org/openlca/core/results/LcaResult.java#L111).
