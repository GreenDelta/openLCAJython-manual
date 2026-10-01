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

- [Create from scratch](create.md)
- [Create from existing flow](from_existing.md)
- [Get from the database](from_database.md)
- [Update with more info](update.md)
- [Parametrize input exchanges](parametrize.md)
- [Add a default provider](add_default_provider.md)
- [Update exchange amount](get_exchange.md)
- [Move to a category](to_category.md)
- [Delete a process](delete.md)
