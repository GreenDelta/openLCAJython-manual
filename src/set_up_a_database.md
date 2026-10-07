# Set up a database

Most scripts read from or write to a database, so you need one open before they do anything useful. If
you are only trying things out, an empty database with reference data and the standard LCIA methods is a
good starting point.

## Create a database with reference data

In the menu, go to `Database → New database → From scratch...`, enter a name, and select **Complete
reference data** before clicking **Finish**.

This creates a database containing the reference data — units, flow properties, and so on. For more
detail, see
[Creating a new database from scratch](https://greendelta.github.io/openLCA2-manual/databases/create_database.html#creating-a-new-database-from-scratch).

## Import the LCIA methods

Download the openLCA LCIA methods package from Nexus and import it into the database you just created.
For more detail, see
[Importing LCIA methods into openLCA](https://greendelta.github.io/openLCA2-manual/lcia_methods/importing_lcia_methods.html).

## A ready-made alternative

The database above starts empty of content: it has reference data and methods, but no processes or
product systems — you create those yourself. If you would rather begin with real data to explore and
calculate, the free [BAFU database](https://nexus.openlca.org/downloads) on Nexus is one option; a few
of the [examples](examples/README.md) use it.

## You are ready

Open the database. The `db` variable in your scripts now refers to it. Continue with
[A minimal example](minimal_example.md).
