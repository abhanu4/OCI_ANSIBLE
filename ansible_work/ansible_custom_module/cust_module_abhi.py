#!/bin/python
module_args = dict(
compartment_id=dict(type='str', Required=False)
)
print('#########################')

print(module_args)

print('#########################')

module_args.update(dict(policy_id=dict(type='str', Required=False)))

print(module_args)



