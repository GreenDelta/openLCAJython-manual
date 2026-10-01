# Process

A process is a set of interrelated activities that takes place within the life cycle of a product or
system, and transforms inputs into outputs. A process can be a manufacturing process, a transportation
activity, an energy generation process, or any other operation within the life cycle. Processes are
defined by their quantitative reference, which represents the amount of product or service that the
process provides. For example, a process could be the set of all inputs and outputs occurring in the
production of 1 kg of PET granulate.

openLCA distinguishes two types of processes:

- **Unit process:** A unit process is the smallest (least aggregated) unit in a production system, for
  which input and output data are quantified. It can contain any flow type.
- **System process:** A system process is an aggregated life cycle result saved as a process.

_Source: [openLCA 2 manual — Processes](https://greendelta.github.io/openLCA2-manual/processes/index.html)_

In scripts, a process describes the inputs and outputs (exchanges) related to a quantitative reference
which is typically the output product of the process.

<svg viewBox="0 0 400 320" role="img" aria-label="A product system references processes; a process has exchanges that reference flows" style="max-width:400px;width:100%;height:auto;font-family:sans-serif">
  <title>Process, exchanges, flows and product system</title>
  <defs>
    <marker id="af2" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
      <path d="M0,0 L8,4 L0,8 z" fill="currentColor"/>
    </marker>
  </defs>
  <g fill="none" stroke="currentColor" stroke-width="1.5">
    <rect x="90" y="14" width="220" height="48" rx="6"/>
    <rect x="100" y="92" width="200" height="48" rx="6"/>
    <rect x="90" y="170" width="220" height="48" rx="6"/>
    <rect x="120" y="248" width="160" height="40" rx="6"/>
    <line x1="200" y1="62" x2="200" y2="90" marker-end="url(#af2)"/>
    <line x1="200" y1="140" x2="200" y2="168" marker-end="url(#af2)"/>
    <line x1="200" y1="218" x2="200" y2="246" marker-end="url(#af2)"/>
  </g>
  <g fill="currentColor">
    <text x="200" y="34" text-anchor="middle" font-size="14">ProductSystem</text>
    <text x="200" y="52" text-anchor="middle" font-size="10" opacity="0.7">reference process + links</text>
    <text x="200" y="112" text-anchor="middle" font-size="14">Process</text>
    <text x="200" y="130" text-anchor="middle" font-size="10" opacity="0.7">unit / system process</text>
    <text x="200" y="190" text-anchor="middle" font-size="13">Exchange (input / output)</text>
    <text x="200" y="208" text-anchor="middle" font-size="10" opacity="0.7">amount · unit</text>
    <text x="200" y="272" text-anchor="middle" font-size="14">Flow</text>
    <text x="208" y="80" font-size="11" opacity="0.85">referenceProcess</text>
    <text x="208" y="158" font-size="11" opacity="0.85">exchanges</text>
    <text x="208" y="236" font-size="11" opacity="0.85">flow</text>
    <text x="200" y="308" text-anchor="middle" font-size="10" opacity="0.7">The quantitative reference is the process's product output exchange.</text>
  </g>
</svg>

_A `ProductSystem` is built from a reference `Process` and links to others; each `Process` holds
input/output `Exchange`s that reference `Flow`s._

- [Create from scratch](create.md)
- [Create from existing flow](from_existing.md)
- [Get from the database](from_database.md)
- [Update with more info](update.md)
- [Parametrize input exchanges](parametrize.md)
- [Add a default provider](add_default_provider.md)
- [Update exchange amount](get_exchange.md)
- [Move to a category](to_category.md)
- [Delete a process](delete.md)
