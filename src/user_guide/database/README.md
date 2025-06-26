# Interacting with the database

To do anything meaningful in openLCA via scripting—like accessing flows, processes, product systems,
or results—you need to interact with the database. This chapter introduces the main ways to do that:

- Using the db variable, a pre-defined connection to the currently opened database.

- Accessing data through DAOs (Data Access Objects), the recommended and structured way to query
  model elements.

- Writing custom SQL queries for advanced or performance-critical operations.
