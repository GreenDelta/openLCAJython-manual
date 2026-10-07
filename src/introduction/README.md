# Introduction

This is a guide to automating openLCA: doing in seconds, with a few lines of instructions, what would
otherwise be an afternoon of clicking — bulk edits, calculations across many systems, custom exports.
It does assume some basic programming knowledge — the examples are written in Python, so a little prior
experience with Python (or any language) will make them much easier to follow.

To start right away, go to the [Quickstart](../quickstart.md).

## What you can do with it

Common uses include:

- **Calculate many product systems at once** and write the results to a single spreadsheet, rather than
  running and exporting them individually.
  ([Batch calculate to Excel](../examples/batch_calculate_to_excel.md))
- **Test sensitivity** by running a system repeatedly with different parameter values.
  ([Sensitivity analysis](../calculate/sensitivity_analysis.md))
- **Edit data in bulk** — rename, recategorize, or correct the same field across hundreds of processes
  in a single pass. ([Update a process](../process/update.md))
- **Build models from a spreadsheet**, creating flows, processes, and product systems from existing
  data. ([Create a flow](../flow/create.md), [a process](../process/create.md),
  [a product system](../product_system/create.md))
- **Produce custom reports** in the layout you need. ([Excel automation](../examples/excel_automation.md))

## Is this the right tool for me?

You write your scripts in an editor built into openLCA, so there is nothing to install. openLCA includes
Python (called Jython) and runs your scripts directly.

If you are an experienced Python developer, you may prefer openLCA's
[IPC API](https://greendelta.github.io/openLCA-ApiDoc/), which lets you control openLCA from your own
Python installation.

## Before you start

Scripts write directly to your database, creating, editing, and deleting datasets, and those changes are
not easily undone. Work on a copy of your database until you are confident that a script behaves as
intended.

The [Quickstart](../quickstart.md) covers writing and running your first script.
