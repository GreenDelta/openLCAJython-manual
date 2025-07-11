# Analysis groups

With analysis groups, you can categorize your product system's processes into various categories
allowing later to group results (see
[openLCA manual](https://greendelta.github.io/openLCA2-manual/res_analysis/res_analysis_groups)).

## Get the analysis groups

The `AnalysisGroup` type contains the name and color of the analysis group and a set of processes.

```python
class AnalysisGroup:
    name: str
    color: str
    processes: Set[long]  # set of processes id
```

You can get the analysis groups information from the product system as follows:

```python
form java.util import HashSet

for group in system.analysisGroups:
    print("%s (%s)" % (group.name, group.color))
    for process in HashSet(group.processes):
        print(" - %s" % process)
```

## Get the results for an analysis group

You can get the results for an analysis group as follows:

```python
grouped_result = AnalysisGroupResult.of(system, result)
for category in categories:
    impact_values = grouped_result.getResultsOf(Descriptor.of(category))
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
