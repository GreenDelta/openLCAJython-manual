# Analysis groups

With analysis groups, you can categorize your product system's processes into various categories
allowing later to group results (see
[openLCA manual](https://greendelta.github.io/openLCA2-manual/res_analysis/res_analysis_groups)).

## Get the analysis groups

The `AnalysisGroup` object contains the `name` and `color` of the analysis group and a set of `processes` IDs.

You can get the analysis groups information from the product system as follows:

```python
# import the HashSet class to work with the set of processes
from java.util import HashSet

for group in system.analysisGroups:
    print("%s (%s)" % (group.name, group.color))
    # loop over the set of processes
    for process in HashSet(group.processes):
        print(" - %s" % process)
```

## Get the results for an analysis group

You can get the results for an analysis group as follows:

```python
# create the analysis group result from the LcaResult
grouped_result = AnalysisGroupResult.of(system, result)
for category in method.impactCategories:
    impact_values = grouped_result.getResultsOf(Descriptor.of(category))
    # The Top group is gather the impact of processes not in any analysis group: the "Rest"
    print(
        "%s (Rest: %s %s):"
        % (category.name, impact_values.get("Top"), category.referenceUnit)
    )
    for group in system.analysisGroups:
        print(
            " - %s: %s %s"
            % (group.name, impact_values.get(group.name), category.referenceUnit)
        )
```
