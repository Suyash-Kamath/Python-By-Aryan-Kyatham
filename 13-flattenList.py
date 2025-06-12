nested_list = ["Hi Krishna ", ["How are you Krishna "], "I hope you are fine "]

flat_list = []

for item in nested_list:
    if isinstance(item,list):
        flat_list.extend(item)
    else:
        flat_list.append(item)

chars = ''.join(flat_list)

print(chars)

'''

 .extend() — What Is It?
.extend() is a method used with lists in Python. It adds elements from an iterable (like another list, tuple, or string) into the existing list.

It does not add the iterable as a single item—it adds each element individually.

.append() adds the entire list item as a single sublist.

.extend() unpacks the list and adds its items individually.
'''



list4 = [1,2]
item = [3,4]

list4.extend(item)

print(list4)