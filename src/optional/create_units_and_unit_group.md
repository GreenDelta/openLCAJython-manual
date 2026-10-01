# Create units and a unit group

All quantitative amounts of the inputs and outputs in a process have a unit of measurement. In
openLCA convertible units are organized in groups that have a reference unit to which the conversion
factors of the units are related.

A unit group is a collection of units for a given flow property.

_Source: [openLCA 2 manual — Database elements](https://greendelta.github.io/openLCA2-manual/databases/database_elements.html)_

```python
# create units for our mass unit group with a name and a conversion factor
kg = Unit.of("kg", 1.0)
g = Unit.of("g", 0.001)

# create a unit group with kilogram as reference unit
units_of_mass = UnitGroup.of("Unit of mass", kg)

# add the unit to the unit group list of units
units_of_mass.units.add(kg)
units_of_mass.units.add(g)

# insert the unit group into the database (no need to insert the units)
db.insert(units_of_mass)

# refresh the navigator to see the new unit group
App.runInUI("Refresh navigator", lambda: Navigator.refresh())
```
