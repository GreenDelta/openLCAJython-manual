MAX_NODES = 50
MIN_SHARE = 0.1

# retrieve the first impact category
category_descriptor = Descriptor.of(method.impactCategories[0])
sankey = (
    Sankey.of(impact_descriptor, result.provider())
    .withMinimumShare(MIN_SHARE)
    .withMaximumNodeCount(MAX_NODES)
    .build()
)
