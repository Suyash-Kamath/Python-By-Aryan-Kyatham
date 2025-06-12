'''
Step-by-Step Explanation:
text = "Hi SUYASH"
Creates a string object and stores it in a variable called text.

The string is: "Hi SUYASH" (a sequence of 9 characters including a space).

Internally, it's stored in memory like this:

['H', 'i', ' ', 'S', 'U', 'Y', 'A', 'S', 'H']

ascii_values = [ord(char) for char in text]
This is a list comprehension, and it's a compact way to build a list.

It means:

For every character (char) in the string text

Apply the function ord(char) to get its ASCII/Unicode value

Collect those values into a new list

'''

text = "Hi SUYASH"
# ascii_values = [ord(char) for char in text]
# print(ascii_values)

# Internally it does this

ascii_values = []
for char in text:
    ascii_code = ord(char)
    ascii_values.append(ascii_code)

print(ascii_values)


# ------------------------------------------------------------------------------------------------------------------------------


# print(chr(49))
ascii_list = [72, 105, 32, 83, 117, 121, 97, 115, 104]

# chars = ''.join([chr(num) for num in ascii_list])

# print(chars)


'''
chars = ''.join([chr(num) for num in ascii_list])
This line:

Converts each number in the list into its character using chr(num)

Then joins them all together into a single string using ''.join(...)

'''


chars_list = []

for num in ascii_list:
    character = chr(num)
    chars_list.append(character)

chars = ''.join(chars_list)

print(chars)