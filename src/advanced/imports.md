# What you can import

Beyond the openLCA classes that are [available without any import](../how_scripts_run.md), you can
import more into a script. Here is what is and isn't available.

## Java classes

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
