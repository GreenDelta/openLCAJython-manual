# To go further

## Java source code

### The olca-modules repository

You can find the detail of every data type of openLCA in the source code of the application. The
repository is open source and you can browse the code yourself. The repository is available at
[github.com/GreenDelta/olca-modules](https://github.com/GreenDelta/olca-modules/).

The module containing the data model of openLCA is called `olca-core`. You can find the folder with
all the classes in
[`model`](https://github.com/GreenDelta/olca-modules/tree/master/olca-core/src/main/java/org/openlca/core/model).

### Example

For example, if you wonder how to add normalization and weighting set to an impact method, you can
find how to create a normalization and weighting set and add it.

1. find the
   [`ImpactMethod`](https://github.com/GreenDelta/olca-modules/blob/master/olca-core/src/main/java/org/openlca/core/model/ImpactMethod.java)
   class and check how to add a normalization and weighting set. In that case, you will use the
   `ImpactMethod.add(nwSet)  # nwSet: NwSet` method.
1. find the
   [`NwSet`](https://github.com/GreenDelta/olca-modules/blob/master/olca-core/src/main/java/org/openlca/core/model/NwSet.java)
   class and check how to build it with `NwSet.of(name) # name: str` method.
1. realize that you need to add `factor` to this new `NwSet` instance with the
   `NwSet.add(factor) # factor: NwFactor` method.
1. check out the
   [`NwFactor`](https://github.com/GreenDelta/olca-modules/blob/master/olca-core/src/main/java/org/openlca/core/model/NwFactor.java)
   class and find how to create it with the
   `NwFactor.of(impact, normalisationFactor, weightingFactor) # impact: ImpactCategory, normalisationFactor: float, weightingFactor: float`

You can now create and add a normalization and weighting set to an impact method with the following
code:

```python
nwSet = NwSet.of("My new normalization and weighting set")
nwSet.add(NwFactor.of(category_one, 4.2, 0.042))
nwSet.add(NwFactor.of(category_two, 2.4, 0.024))

method.add(nwSet)
```

### Java first, then Jython

One helpful approach when working with Jython is to first write your code in Java and then translate
it to Python syntax. This method can be very effective if you already have some experience with
Java, as it allows you to reuse your knowledge of Java classes, method calls, and structure. You can
use any Java IDE (like Eclipse or IntelliJ) to write your Java code first, which often makes
debugging easier. Once your Java version looks good, you can convert it step by step into Python
code that runs on the Jython interpreter.
