# Contribution tree

As you probably know from using the _Contribution tree_ tab in openLCA, it is a visual
representation of the environmental impacts of a system across its entire supply chain. It helps
identify which stages of the life cycle contribute most to the overall environmental impact.

The contribution tree can be obtained from the `LcaResult` object by using the `UpstreamTree.of`
method. It takes a `ResultProvider` as well as an `EnviFlow` or `ImpactDescriptor` (see
[Advanced data model](../data_model/advanced_data_model.md)) object as input. Let's build one:

## Getting an upstream tree

```python
climate_change = next(i for i in method.impactCategories if i.name == "Climate change")
tree = UpstreamTree.of(result.provider(), Descriptor.of(climate_change))
```

The `UpstreamTree` is composed of `UpstreamNode` objects. Each `UpstreamNode` provides different
types of result and the provider (`TechFlow`). The root node of the tree can be retrieved via the
`UpstreamTree.root` attribute. And the children of a node can be retrieved via the
`UpstreamTree.childs` method.

```python
class UpstreamNode
    def provider(): # () -> TechFlow
        """Returns the provider of the product output or waste input of this upstream tree node."""
    def result(): # () -> float
        """Returns the upstream result of this node."""
    def requiredAmount(): # () -> float
        """Returns the required amount of the provider flow of this upstream node."""
    def scalingFactor(): # () -> float
        """Returns the scaling factor of this upstream node."""
    def directContribution(): # () -> float
        """
        Returns the direct contribution of the process (tech-flow) of the node to the total
        result the node.
        """
```

## Traversing the tree, breath-first

The tree can be traversed using the `UpstreamTree.childs` method recursively. A good practice is to
set a maximum depth to avoid long computation times.

```python
DEPTH = 5
UNIT = climate_change.referenceUnit

def traverse(tree, node, depth):
    if depth == 0:
        return
    print(
        "%sThe impact result of %s is %s %s (%s%%)."
        % (
            "  " * (DEPTH - depth),
            node.provider().provider().name,
            node.result(),
            UNIT,
            node.result() / tree.root.result() * 100,
        )
    )
    for child in tree.childs(node):
        traverse(tree, child, depth - 1)


traverse(tree, tree.root, DEPTH)
```
