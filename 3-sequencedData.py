

'''

🔹 What is a List in Python?
A list is:

An ordered collection of items.

Mutable (you can change, add, or remove items).

Can contain any type of data, including other lists → this is called a nested list.

 List
 List: An ordered collection of data with elements separated by commas and enclosed within square brackets.
 Lists are mutable and can be modified.
The square brackets [] indicate a list in Python.

list1 = ['B', 2.3, [-4, 5], ['apple']]
Yes, this is a list, not an array. The square brackets [] indicate a list in Python.

In this example:

'B' → a string

2.3 → a float

[-4, 5] → a nested list (a list inside a list)

['apple'] → another nested list


------------------------------------------------------


🔹 What is a Tuple in Python?
A tuple is:

Also an ordered collection of items.

But it is immutable (once created, you cannot change or modify it).

Defined with parentheses ().

| Feature     | List                   | Tuple                       |
| ----------- | ---------------------- | --------------------------- |
| Syntax      | `[ ]`                  | `( )`                       |
| Mutability  | ✅ Mutable (can change) | ❌ Immutable (cannot change) |
| Performance | Slightly slower        | Slightly faster             |
| Use Case    | Dynamic data           | Fixed, constant data        |
| Nesting     | Supports nested lists  | Supports nested tuples      |



| Use Case                                                   | Use a **List** if...  | Use a **Tuple** if... |
| ---------------------------------------------------------- | --------------------- | --------------------- |
| You want to change, add, or delete items                   | ✅ Yes                 | ❌ No                  |
| You’re storing sensor data, live updates, dynamic values   | ✅ Yes                 | ❌ No                  |
| You’re storing coordinates, fixed config, or readonly info | ❌ Not ideal           | ✅ Yes                 |
| You're passing data as keys in a dictionary                | ❌ Lists can't be keys | ✅ Tuples can be keys  |




'''

list = ['B',2.30,[-4,5],['apple']]

print(list)

tuple = ("Suyash","Kamath",("Hi How"),("are you"))

print(tuple)


cart = ['milk', 'bread']
cart.append('eggs')  # ✅ works


location = (19.0760, 72.8777)  # Mumbai coordinates
# location[0] = 20.0 ❌ Not allowed

print(cart)