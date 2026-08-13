# Advanced

- [Technosphere flows](technosphere_flows.md)
- [Intervention flows](intervention_flows.md)
- [Impact categories](impact_categories.md)
- [Contribution tree](contribution_tree.md)
- [Costs](costs.md)
- [Analysis groups](analysis_groups.md)
- [Sankey graph](sankey_graph.md)

## `LcaResult` object

The result of the calculation is a `LcaResult` object. It provides an interface for accessing impact
factors, total flows, and contributions and many other objects in a structured way. The manual won't
cover all the accessible methods of the `LcaResult` object. For more information, please refer to
the
[class](https://github.com/GreenDelta/olca-modules/blob/master/olca-core/src/main/java/org/openlca/core/results/LcaResult.java#L82)
itself.

For the following examples, let's assume we have calculated the results of a product system under
the Python variable `result`.
