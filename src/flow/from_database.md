# Get flows from the database

You can retrieve a flow by its name or UUID, fetch its lightweight descriptor, or load every flow in
the database at once.

```python
# get and print the flow by name
flow_by_name = db.getForName(Flow, "Aluminium ingot")
print(flow_by_name)

# get and print the flow by id (copy the UUID from the openLCA flow page)
flow_by_id = db.get(Flow, "UUID_of_the_flow")
print(flow_by_id)

# get and print the descriptor of a flow (smaller object)
flow = db.getDescriptor(Flow, "UUID_of_the_flow")
print(flow)

# get and print all the database flows (can take a while)
flows = db.getAll(Flow)
for flow in flows:
    print(flow)

# get and print all the database flow descriptors (can take a while)
flow_descriptors = db.getDescriptors(Flow)
for flow_descriptor in flow_descriptors:
    print(flow_descriptor)
```
