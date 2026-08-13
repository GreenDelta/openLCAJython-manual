# Meta classes

## RootEntity

The `RootEntity` is the base class for all entities (flows, processes, units, unit groups, ...). A
`RefEntity` is an entity that can be referenced by a unique ID, the reference ID or short `refId`.

```python
class RootEntity:
    name: str
    refId: str
    description: str
    ...
```

## Descriptors

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

## FlowDescriptor

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

## LocationDescriptor

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

## ImpactDescriptor

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
