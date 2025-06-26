# Advanced data model

## Categories

```python
class Category:
    name: str
    modelType: ModelType
    category: Category
    childCategory: List[Category]
    ...
```

A category is a path that is used to group entities (flows, processes, ...) together. For example,
the category of a flow `Emission to air/unspecified/Chromium VI` is `unspecified` and the category
of `unspecified` is `Emission to air`:

```python
print(chromium6.category.name) # prints: unspecified
print(chromium6.category.category.name) # prints: Emission to air
```

To create a category, we use the `Category.of` and `Category.childOf` method:

```python
emission = Category.of("Emission to air", Flow)
unspecified = Category.childOf(emission, "unspecified")
chromium6.category = unspecified
```

## Parameters

In openLCA, parameters can be defined in different scopes: global, process, or LCIA method. The
parameter name can be used in formulas and, thus, need to conform to a specific syntax. Within a
scope the parameter name should be unique (otherwise the evaluation is not deterministic). There are
two types of parameters in openLCA: input parameters and dependent parameters. An input parameter
can have an optional uncertainty distribution but not a formula. A dependent parameter can (should)
have a formula (where also other parameters can be used) but no uncertainty distribution.

```python
class Parameter:
    name: str
    scope: ParameterScope
    isInputParameter: bool
    value: float
    uncertainty: Uncertainty
    formula: str
    ...
```

Parameters can be created in the following way:

```python
# create a global input parameter
g = Parameter.global("number_of_items", 42.0) # name: str, value: float

# create a process input parameter
process = Process()
p = Parameter.process("output_volume", 2.4) # name: str, value: float

# create a LCIA method dependent parameter
# name: str, formula: str
impact_category = ImpactCategory()
i = Parameter.impact("impact_value", "2 * number_of_items")
```

## Meta classes

### RootEntity

The `RootEntity` is the base class for all entities (flows, processes, units, unit groups, ...). A
`RefEntity` is an entity that can be referenced by a unique ID, the reference ID or short `refId`.

```python
class RootEntity:
    name: str
    refId: str
    description: str
    ...
```

### Descriptors

Descriptors are lightweight models containing only descriptive information of a corresponding
entity. The intention of descriptors is to get this information fast from the database without
loading the complete model. Checkout the [Interacting with the database](../database) chapter for
more information.

```python
class Descriptor: # or RootDescriptor
    name: str
    refId: str
    version: long
    lastChange: long
    library: str  # contains the library identifier
    tags: str
    type: ModelType
    ...
```

#### FlowDescriptor

The `FlowDescriptor` class extends the `RootDescriptor` class and adds the flow type, location as
well as the reference flow property ID.

```python
class FlowDescriptor:
    name: str
    refId: str
    version: long
    lastChange: long
    library: str  # contains the library identifier
    tags: str
    type: ModelType
    flowType: FlowType
    location: long
    refFlowPropertyId: long
    ...
```

#### LocationDescriptor

The `LocationDescriptor` class extends the `RootDescriptor` class and adds the location code.

```python
class LocationDescriptor:
    name: str
    refId: str
    version: long
    lastChange: long
    library: str  # contains the library identifier
    code: str
```

#### ImpactDescriptor

The `ImpactDescriptor` class extends the `RootDescriptor` class and adds the reference unit and the
direction.

```python
class ImpactDescriptor:
    name: str
    refId: str
    version: long
    lastChange: long
    library: str  # contains the library identifier
    referenceUnit: str
    direction: Direction
```
