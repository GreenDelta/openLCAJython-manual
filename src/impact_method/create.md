# Create an impact method from scratch

The following code snippets are probably not very useful. You will probably import LCIA methods into
your database rather than creating them from scratch.

```python
# get the mass flow property from the database to create elementary flows
mass = db.getForName(FlowProperty, "Mass")

# create a flow for the bromopropane and butane
bromopropane = Flow.elementary("Bromopropane", mass)
butane = Flow.elementary("Butane", mass)

# create an impact category
impact_category = ImpactCategory.of("Climate change", "kg CO2-Eq")

# add the impact factors for bromopropane and butane
impact_category.factor(bromopropane, 0.052)
impact_category.factor(butane, 0.006)

# create an impact method with (only) one impact category
impact_method = ImpactMethod.of("EF 3.0")
impact_method.add(impact_category)

# insert the datasets into the database
db.insert(bromopropane, butane, impact_category, impact_method)

# refresh the navigator to see the new flows
App.runInUI("Refresh navigator", lambda: Navigator.refresh())
```
