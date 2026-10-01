# Contribution tree

As you probably know from using the _Contribution tree_ tab in openLCA, it is a visual
representation of the environmental impacts of a system across its entire supply chain. It helps
identify which stages of the life cycle contribute most to the overall environmental impact.

The contribution tree can be obtained from the `LcaResult` object by using the `UpstreamTree.of`
method. It takes a `ResultProvider` as well as an `EnviFlow` or `ImpactDescriptor` (see
[Meta classes](../../advanced/meta_classes.md#impactdescriptor)) object as input. Let's build one:

## Getting an upstream tree

Build the tree from the result provider and the descriptor of the impact category you want to inspect.

```python
# retrieve the first impact category
category = method.impactCategories[0]
tree = UpstreamTree.of(result.provider(), Descriptor.of(category))
```

The `UpstreamTree` is composed of `UpstreamNode` objects. Each `UpstreamNode` provides different
types of result and the provider (`TechFlow`). The root node of the tree can be retrieved via the
`UpstreamTree.root` attribute. And the children of a node can be retrieved via the
`UpstreamTree.childs` method.

- `provider()`: Returns the provider of the product output or waste input of this upstream tree
  node.
- `result()`: Returns the upstream result of this node.
- `requiredAmount()`: Returns the required amount of the provider flow of this upstream node.
- `scalingFactor()`: Returns the scaling factor of this upstream node.
- `directContribution()`: Returns the direct contribution of the process (tech-flow) of the node to
  the total result the node.

## Traversing the tree, breath-first

The tree can be traversed using the `UpstreamTree.childs` method recursively. A good practice is to
set a maximum depth to avoid long computation times.

```python
# retrieve the first impact category
category = method.impactCategories[0]
tree = UpstreamTree.of(result.provider(), Descriptor.of(category))

DEPTH = 5
UNIT = category.referenceUnit

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
    # recursively traverse the tree
    for child in tree.childs(node):
        traverse(tree, child, depth - 1)


traverse(tree, tree.root, DEPTH)
```
