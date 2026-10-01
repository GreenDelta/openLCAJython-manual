# Parametrize impact category

Parameters can be used in the same way for LCIA categories as for
[processes](../process/parametrize.md).

_Source: [openLCA 2 manual — Parameters](https://greendelta.github.io/openLCA2-manual/lcia_methods/impcat_parameters.html)_

```python
# let's say we already have the following impact method in the database
# get the mass flow property from the database to create elementary flows
mass = db.getForName(FlowProperty, "Mass")
bromopropane = Flow.elementary("Bromopropane", mass)
butane = Flow.elementary("Butane", mass)
impact_category = ImpactCategory.of("Climate change", "kg CO2-Eq")
uuid = impact_category.refId
impact_category.factor(bromopropane, 0.052)
impact_category.factor(butane, 0.006)
impact_method = ImpactMethod.of("EF 3.0")
impact_method.add(impact_category)

# insert the datasets into the database
db.insert(bromopropane, butane, impact_category, impact_method)

# get the impact category from the database
category = db.get(ImpactCategory, uuid)

impact_factor = next(f for f in category.impactFactors if f.flow.name == "Bromopropane")
pressure = Parameter.impact("pressure", 1.01)
impact_factor.formula = "0.052 * " + pressure.name + " / 1.01"
impact_factor.value = 0.052 * pressure.value / 1.01
category.parameters.add(pressure)

# increase the version and update the last update date
Version.incUpdate(category)  # or incMinor/incMajor to increase minor/major version
# update the flow in the database
db.update(category)

# refresh the navigator to see the new flows
App.runInUI("Refresh navigator", lambda: Navigator.refresh())
```
