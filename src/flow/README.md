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

<svg viewBox="0 0 360 300" role="img" aria-label="A flow references a flow property, which uses a unit group that contains units" style="max-width:360px;width:100%;height:auto;font-family:sans-serif">
  <title>Flow, flow property, unit group and units</title>
  <defs>
    <marker id="af1" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
      <path d="M0,0 L8,4 L0,8 z" fill="currentColor"/>
    </marker>
  </defs>
  <g fill="none" stroke="currentColor" stroke-width="1.5">
    <rect x="80" y="14" width="200" height="50" rx="6"/>
    <rect x="90" y="96" width="180" height="40" rx="6"/>
    <rect x="90" y="168" width="180" height="40" rx="6"/>
    <rect x="80" y="240" width="200" height="50" rx="6"/>
    <line x1="180" y1="64" x2="180" y2="94" marker-end="url(#af1)"/>
    <line x1="180" y1="136" x2="180" y2="166" marker-end="url(#af1)"/>
    <line x1="180" y1="208" x2="180" y2="238" marker-end="url(#af1)"/>
  </g>
  <g fill="currentColor">
    <text x="180" y="36" text-anchor="middle" font-size="14">Flow</text>
    <text x="180" y="54" text-anchor="middle" font-size="10" opacity="0.7">elementary · product · waste</text>
    <text x="180" y="121" text-anchor="middle" font-size="14">FlowProperty</text>
    <text x="180" y="193" text-anchor="middle" font-size="14">UnitGroup</text>
    <text x="180" y="262" text-anchor="middle" font-size="14">Unit</text>
    <text x="180" y="280" text-anchor="middle" font-size="10" opacity="0.7">reference unit + conversions</text>
    <text x="188" y="84" font-size="11" opacity="0.85">referenceFlowProperty</text>
    <text x="188" y="156" font-size="11" opacity="0.85">unitGroup</text>
    <text x="188" y="230" font-size="11" opacity="0.85">units</text>
  </g>
</svg>

_A `Flow` has a type and a reference `FlowProperty`; the flow property points to a `UnitGroup`, which
holds its units (one reference unit plus conversions)._

- [Create from scratch](create.md)
- [Get from the database](from_database.md)
- [Update with more info](update.md)
- [Move to a category](to_category.md)
- [Delete a flow](delete.md)
