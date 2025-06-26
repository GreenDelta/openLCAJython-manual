# Building a product system from a process

openLCA provides the option to create a product system from a process. The same operation can be
done from the Python editor as well. Similar settings (preferred providers, process type) can be set
with the `LinkingConfig` object. To run the following code in the openLCA Python editor, you need to
open an ecoinvent database (here ecoinvent v3.10.1 APOS).

```python
process = db.getForName(Process, "gold production | gold | APOS, U")
if not isinstance(process, Process):
    raise Exception("Process not found")

config = (
    LinkingConfig()
    .providerLinking(ProviderLinking.PREFER_DEFAULTS)
    .preferredType(LinkingConfig.PreferredType.UNIT_PROCESS)
)

system = ProductSystemBuilder(db, config).build(process)
```

Once again, you need to run `db.insert(system)` to store the product system in the database.

The `ProviderLinking` indicates how default providers of product inputs or waste outputs in
processes should be considered in the linking of a product system. It is define as follows:

```python
class ProviderLinking(Enum):
    IGNORE_DEFAULTS,
    PREFER_DEFAULTS,
    ONLY_DEFAULTS,
```

- `IGNORE_DEFAULTS`: Default provider settings are ignored in the linking process. This means that
  the linker can also select another provider even when a default provider is set.
- `PREFER_DEFAULTS`: When a default provider is set for a product input or waste output the linker
  will always select this process. For other exchanges it will select the provider according to its
  other rules.
- `ONLY_DEFAULTS`: Means that links should be created only for product inputs or waste outputs where
  a default provider is defined which are then linked exactly to this provider.

The `PreferredType` indicates which type of process should be used to link the product system. It is
defined as follows:

```python
enum PreferredType(Enum):
    UNIT_PROCESS,
	SYSTEM_PROCESS,
    RESULT
```
