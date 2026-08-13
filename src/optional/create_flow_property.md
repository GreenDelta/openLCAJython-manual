# Create a flow property

A flow in openLCA has physical properties (like mass or volume), called flow properties, in which
the amount of a flow in a process exchange can be specified.

The following example creates a flow property for mass.

```python
# create a unit group for mass
kg = Unit.of("kg", 1.0)
units_of_mass = UnitGroup.of("Unit of mass", kg)
g = Unit.of("g", 0.001)
units_of_mass.units.add(g)

# create a flow property with the default flow property type PHYSICAL
mass = FlowProperty.of("Mass", units_of_mass)

# insert the flow property and the unit group into the database
db.insert(units_of_mass, mass)

# refresh the navigator to see the new flow property
App.runInUI("Refresh navigator", lambda: Navigator.refresh())
```

When creating an economic flow property, set the flow property type to `ECONOMIC`.

```python
# create a unit group for market value
dollar = Unit.of("USD", 1.0)
units_of_currency = UnitGroup.of("Unit of currency", dollar)
euro = Unit.of("EUR", 0.86)
units_of_currency.units.add(euro)

# create a flow property with the flow property type ECONOMIC
market_value = FlowProperty.of("Market value", units_of_currency)
market_value.flowPropertyType = FlowPropertyType.ECONOMIC

# insert the flow property and the unit group into the database
db.insert(units_of_currency, market_value)

# refresh the navigator to see the new flow property
App.runInUI("Refresh navigator", lambda: Navigator.refresh())
```
