# Flow

Flows represent products and materials that move throughout a life cycle, interconnected within the
process network, and take form of inputs, outputs, energy, or emissions. Flows can be substances,
products, materials, energy carriers, emissions, or other types of inputs or outputs. A flow is
characterized by its name, flow type, and reference flow property (unit category in which the flow is
expressed). Examples of flows include electricity, water, CO2 emissions, aluminium, and so on.

In general, openLCA distinguishes three flow types:

- **Elementary flows:** These flows represent material or energy entering the system that has been
  drawn from the environment without previous human transformation, or material or energy leaving the
  system and released into the environment without further human transformation. For example, crude
  oil extracted from the ground, or emissions released into the air.
- **Product flows:** These are all the flows that are not elementary or waste flows, and represent the
  materials or energy exchanged between processes within the product system.
- **Waste flows:** Waste flows are any substances or objects that the holder needs to dispose of, like
  by-products with no market value or those requiring more resources to recycle than their economic
  return.

Each flow created in openLCA must be associated with a reference flow property, such as mass, volume,
area, and so on. Though, it is also possible to have multiple flow properties for the same flow (e.g.
uranium can be measured using both mass and radioactivity units, gasses can be measured using both
mass and volume units, etc.)

> _**Note**:_ Certain waste flows can also be modelled as product flows. In databases this is usually
> stated in the name. Waste paper is a great example. As it can be used in the production of paper,
> waste paper isn't necessarily modelled as a waste flow but instead as a product flow.

_Source: [openLCA 2 manual — Flows](https://greendelta.github.io/openLCA2-manual/flows/index.html)_

In scripts, flows are the things that are moved around as inputs and outputs (exchanges) of processes.
When a process produces electricity and another process consumes electricity from the first process,
both processes will have an output exchange and an input exchange with a reference to the same flow.

- [Create from scratch](create.md)
- [Get from the database](from_database.md)
- [Update with more info](update.md)
- [Move to a category](to_category.md)
- [Delete a flow](delete.md)
