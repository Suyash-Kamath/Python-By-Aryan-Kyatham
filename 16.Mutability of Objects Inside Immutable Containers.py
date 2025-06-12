'''


The tuple is the immutable container — its structure can’t be changed.

But it can hold mutable objects like lists.

And those inner objects can be changed even though the outer tuple cannot.

Related Concepts You Can Study:

| Concept                         | Meaning                                                           |
| ------------------------------- | ----------------------------------------------------------------- |
| **Immutability**                | An object cannot be changed after creation (e.g., `tuple`, `str`) |
| **Mutability**                  | An object can be changed after creation (e.g., `list`, `dict`)    |
| **Shallow Copy vs Deep Copy**   | Important when nested mutable objects are involved                |
| **Object References in Python** | Understanding how memory and identities work in such cases        |



Tuples are immutable, meaning:

You cannot change the tuple structure (add/remove/replace elements).

But if a tuple contains a mutable object (like a list), the list itself can be changed.

Tuples protect their structure, but not the contents of mutable objects inside them.
Think of it like this:

“The tuple is like a sealed box. You can’t swap the items inside or pull them out... but if one item inside is a whiteboard, you can still write on it!”

'''

my_tuple = (1, 2, [3, 4, 5])
print(my_tuple)  # (1, 2, [3, 4, 5])

# Modify the list inside the tuple
my_tuple[2][0] = 99
print(my_tuple)  # (1, 2, [99, 4, 5])



'''
✅ This works because:

You're not changing the tuple itself.

You're modifying the content of the list inside the tuple.
❌ What You Can’t Do:
my_tuple[0] = 100  # ❌ Error: 'tuple' object does not support item assignment
my_tuple[2] = [10, 20]  # ❌ Error: still changing tuple structure

| Operation                    | Allowed? | Reason             |
| ---------------------------- | -------- | ------------------ |
| Modify list inside tuple     | ✅ Yes    | List is mutable    |
| Replace entire list in tuple | ❌ No     | Tuple is immutable |
| Add/remove tuple elements    | ❌ No     | Tuple is immutable |

'''

t = [10,[20,30],"Suyash"]

t[1].append(99)

print(t)

# Replace list itself (❌)
# t[1] = [50, 60]  # This will raise TypeError