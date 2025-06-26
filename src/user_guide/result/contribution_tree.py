climate_change = next(i for i in method.impactCategories if i.name == "Climate change")
tree = UpstreamTree.of(result.provider(), Descriptor.of(climate_change))

DEPTH = 3
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
