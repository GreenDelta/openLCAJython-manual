# Get processes from the database

```python
# get and print the process by name
process_by_name = db.getForName(Process, "Aluminium ingot")
print(process_by_name)

# get and print the process by id (copy the UUID from the openLCA process page)
process_by_id = db.get(Process, "UUID_of_the_process")
print(process_by_id)

# get and print the descriptor of a process (smaller object)
process = db.getDescriptor(Process, "UUID_of_the_process")
print(process)

# get and print all the database processes (can take a while)
processes = db.getAll(Process)
for process in processes:
    print(process)

# get and print all the database process descriptors (can take a while)
process_descriptors = db.getDescriptors(Process)
for process_descriptor in process_descriptors:
    print(process_descriptor)
```
