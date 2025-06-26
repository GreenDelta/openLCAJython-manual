# Sankey graph

openLCA provides an API to gather all the data necessary to create a Sankey graph. The `Sankey`
class provides methods to gather this data. The Sankey diagram can be created to show the flow of
material as well as impacts in the product system. Here is an example of how to extract the data for
a maximum number of nodes `MAX_NODES` and a minimum share (relative impact of a provider on the
total impacts) `MIN_SHARE`.

First step is to build the Sankey diagram:

```python
MAX_NODES = 50
MIN_SHARE = 0.1
climate_change = next(c for c in method.impactCategories if c.name == "Climate change")
impact_descriptor = Descriptor.of(climate_change)
sankey = (
    Sankey.of(impact_descriptor, result.provider())
    .withMinimumShare(MIN_SHARE)
    .withMaximumNodeCount(MAX_NODES)
    .build()
)
```

The Sankey diagram can then be traversed to get the data for each node. For that, we use the a
consumer method (this is quite specific to Java). The consumer method accepts the `Sankey.Node`
object and execute some operations with it.

```python
class Sankey.Node:
    index: int
    product: TechFlow
    total: float
    direct: float
    share: float
    providers: List[Sankey.Node]
```

To work with the consumer function, we have to import the `java.util.function.Consumer` class.

```python
from java.util.function import Consumer
from org.openlca.app.util import Labels

class AddNodeConsumer(Consumer):
    def accept(self, node):  # type: (Sankey.Node) -> None
        print("\n %s" % (Labels.name(node.product)))
        print(" ID: %s" % (node.product.provider().id))
        print(" Total impact: %s" % (node.total))
        print(" Direct impact: %s" % (node.direct))
        print(" Relative share: %s" % (node.share))
        print(" Cutoff: %s" % (MIN_SHARE))
        print(" Providers:")
        for n in node.providers:
            print("  %s" % (n.product.provider().id))

sankey.traverse(AddNodeConsumer())
```
