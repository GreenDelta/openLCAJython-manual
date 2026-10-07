# Available classes and imports

This page lists what your scripts can use: the openLCA classes available without any import, how to
explore them, and the additional things you can import.

## Classes available without an import

openLCA makes much of its own API available automatically — you can use these directly, no `import`
needed:

- **Core data model** — `Flow`, `FlowProperty`, `Unit`, `UnitGroup`, `Process`, `Exchange`,
  `ProductSystem`, `ImpactMethod`, `ImpactCategory`, `ImpactFactor`, `Parameter`, `Location`,
  `Category`, `Currency`, `NwSet`, `NwFactor`, `Result`, `AnalysisGroup`, `Version`, `RootEntity`
- **Enumerations** — `FlowType`, `FlowPropertyType`, `ProcessType`, `AllocationMethod`, `Direction`,
  `ParameterScope`, `ModelType`
- **Parameter redefinitions** — `ParameterRedef`, `ParameterRedefSet`
- **Calculation & results** — `CalculationSetup`, `SystemCalculator`, `LcaResult`, `TechFlow`,
  `TechFlowValue`, `EnviFlow`, `EnviFlowValue`, `ImpactValue`, `UpstreamTree`, `UpstreamNode`, `Sankey`,
  `AnalysisGroupResult`, `TechIndex`, `EnviIndex`, `NwSetTable`
- **Building product systems** — `ProductSystemBuilder`, `LinkingConfig`, `ProviderLinking`
- **Descriptors** — `Descriptor`, `RootDescriptor`, `FlowDescriptor`, `LocationDescriptor`,
  `ImpactDescriptor`
- **Database access** — `ProcessDao`, `FlowDao`, `ProductSystemDao`, `CategoryDao`, `NativeSql`
- **Input/output** — `Excel`
- **openLCA application** — `App`, `Navigator`, `Editors`, `ResultEditor`, `Workspace`

## How to explore a class

The lists above give the names. To see what a class can actually do — its fields and methods — use
either reference:

- **API documentation** (Javadoc) for the version this manual targets:
  [olca-core 2.6.2 API](https://javadoc.io/doc/org.openlca/olca-core/2.6.2) — every class with its
  methods, and easier to read than the source.
- **Source code** on GitHub: the data model lives in the
  [olca-modules repository](https://github.com/GreenDelta/olca-modules/tree/master/olca-core/src/main/java/org/openlca/core/model);
  open a file such as `Flow.java` to read its fields and methods.

## Importing other Java classes

Any Java class on openLCA's classpath can be imported with `from <package> import <Class>`. This
includes:

- the Java standard library (`java.*`, `javax.*`), e.g. `from java.io import FileOutputStream`;
- any openLCA class by its full package, e.g. `from org.openlca.core.model import ProviderType`;
- libraries bundled with openLCA, such as Apache POI for Excel (`org.apache.poi.ss.usermodel`), the
  Eclipse SWT widgets (`org.eclipse.swt.*`), and the SLF4J logger.

## The Python 2.7 standard library

Jython ships with the Python 2.7 standard library, so the common pure-Python modules work out of the
box:

```python
import os, csv, json, datetime, math, re
```

A few standard-library modules that rely on CPython internals are not supported by Jython.

## Your own Python modules

You can add your own Jython-compatible `.py` modules and import them. See
[Create modules](create_modules.md) for where to put them.

## What you cannot import

- **Packages from PyPI are not installed** — there is no `pip` in the openLCA Python editor, so
  third-party packages are not available unless you add pure-Python modules yourself (see above).
- **Libraries with C extensions do not work at all** — because Jython runs on the JVM, it cannot load
  CPython C extensions. This rules out the scientific stack: **NumPy, Pandas, SciPy** and anything that
  depends on them. `pandas` cannot run in Jython.

If you need NumPy, Pandas or similar, run your analysis in regular (C)Python and connect to openLCA
through the [openLCA IPC Python API](https://greendelta.github.io/openLCA-ApiDoc/) instead.
