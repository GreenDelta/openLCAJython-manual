# Create a product system

This code snippet creates a product system that represents the electrolysis of brine and produces
sodium chloride.

A product system is built from a **reference process** — the process that models the last step of your
supply chain, or the last step of a specific chain. From there, the auto-linking function connects
input and output flows between processes to build up the supply chain. In the script below,
`brine_electrolysis` is the reference process passed to `ProductSystemBuilder`.

_Source: [openLCA 2 manual — Creating a new product system](https://greendelta.github.io/openLCA2-manual/prod_sys/Creating.html)_

Inputs:

- 4.2 kg of sodium chloride
- 42.0 m³ of water (elementary flow)

Outputs:

- 1.0 m³ of chlorine gas

```python
# get the mass and volume flow properties from the database
mass = db.getForName(FlowProperty, "Mass")
volume = db.getForName(FlowProperty, "Volume")

# create an output product for the process
chlorine_gas = Flow.product("Chlorine gas", volume)

# create a process with the Chlorine gas as quantitative reference with the
# default amount of 1.0 m3
brine_electrolysis = Process.of("Brine electrolysis", chlorine_gas)

# create the input product flows: 4.2 kg of sodium chloride and 42.0 m3 of
# water
sodium_chloride = Flow.product("Sodium chloride", mass)
brine_electrolysis.input(sodium_chloride, 4.2)
water = Flow.elementary("Water", volume)
brine_electrolysis.input(water, 42.0)

# create process for the sodium chloride
sodium_chloride_production = Process.of(
  "Sodium chloride production",
  sodium_chloride
)

# insert the process and the newly created flows into the database
db.insert(
    chlorine_gas,
    sodium_chloride,
    water,
    sodium_chloride_production,
    brine_electrolysis
)

config = (
    LinkingConfig()
    .providerLinking(ProviderLinking.PREFER_DEFAULTS)
    .preferredType(LinkingConfig.PreferredType.UNIT_PROCESS)
)

system = ProductSystemBuilder(db, config).build(brine_electrolysis)

# insert the product system into the database
db.insert(system)

# refresh the navigator to see the new process
App.runInUI("Refresh navigator", lambda: Navigator.refresh())
```

The `ProviderLinking` indicates how default providers of product inputs or waste outputs in
processes should be considered in the linking of a product system. It can be one of:

- `IGNORE_DEFAULTS`: Default provider settings are ignored in the linking process. This means that
  the linker can also select another provider even when a default provider is set.
- `PREFER_DEFAULTS`: When a default provider is set for a product input or waste output the linker
  will always select this process. For other exchanges it will select the provider according to its
  other rules.
- `ONLY_DEFAULTS`: Means that links should be created only for product inputs or waste outputs where
  a default provider is defined which are then linked exactly to this provider.

The `PreferredType` indicates which type of process should be used to link the product system. It
can be one of:

- `UNIT_PROCESS`,
- `SYSTEM_PROCESS`,
- `RESULT`.
