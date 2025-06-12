'''

 Can a list be used as a key in a dictionary?
No. You cannot use a list as a dictionary key.

 Why?
Because lists are mutable, and dictionary keys must be immutable and hashable.

Error

my_dict = {
    [1, 2, 3]: "Hello"
}

Output:

TypeError: unhashable type: 'list'

| Type                  | Can be a dictionary key?                       | Reason                   |
| --------------------- | ---------------------------------------------- | ------------------------ |
| `int`, `str`, `float` | ✅ Yes                                          | Immutable and hashable   |
| `tuple`               | ✅ Yes (only if it contains immutable elements) | Hashable                 |
| `list`                | ❌ No                                           | Mutable and not hashable |
| `dict`                | ❌ No                                           | Mutable and not hashable |




Why Do Keys Have to Be Immutable?
A dictionary in Python uses a hash table internally. It calculates a hash value for the key to know where to store the value. If the key could change (like a list), the hash would break and corrupt the dictionary.

'''


my_dict = {
    (1, 2, 3): "Coordinates"
}
print(my_dict[(1, 2, 3)])  # Output: Coordinates

# That works because tuples are immutable and hashable.

'''

| Key Type                 | Can be used as dict key? | Reason                      |
| ------------------------ | ------------------------ | --------------------------- |
| `int`, `str`, `float`    | ✅ Yes                    | Immutable & hashable        |
| `list`                   | ❌ No                     | Mutable & unhashable        |
| `tuple` of immutables    | ✅ Yes                    | Immutable & hashable        |
| `tuple` with list inside | ❌ No                     | Because the list is mutable |


key = (1, 2, 3)
my_dict = {key: "valid"}





Error for below code :
key = (1, [2, 3])  # tuple contains a list (mutable)
my_dict = {key: "invalid"}  # ❌ raises TypeError



'''
