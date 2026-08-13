# Create modules

The Jython standard library is extracted to the `python` folder of the openLCA workspace which is by
default located in your user directory `~/openLCA-data-1.4/python`. This is also the location in
which you can put your own Jython 2.7 compatible modules. For example, when you create a file
`tutorial.py` with the following function in this folder:

```python
# ~/openLCA-data-1.4/python/tutorial.py
def the_answer():
    return 42
```

You can then load it in the openLCA script editor:

```python
import tutorial
import org.openlca.app.util.MsgBox as MsgBox

MsgBox.info("The answer is %s!" % tutorial.the_answer())
```
