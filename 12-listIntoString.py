'''

string_variable = 'separator'.join(list_of_strings)
It combines all elements in the list into one string, using the 'separator' string between the elements.

list1 = ["Hi Suyash", "How are you", "?"]
chars = ' '.join(list1)
print(chars)

 What’s happening:
You're doing:

' '.join(["Hi Suyash", "How are you", "?"])


Which Means

"Hi Suyash" + ' ' + "How are you" + ' ' + "?" = "Hi Suyash How are you ?"

output is 

Hi Suyash How are you ?

🧠 Why it works:
All elements in the list are strings.

join() takes each item in the list and inserts the given separator (here ' ') between them.

Then it returns a new single string.

The list passed to .join() must only contain strings, otherwise Python throws an error like:

TypeError: sequence item 1: expected str instance, list found


Summary:
join() merges list of strings into one string.

The string before .join() is the separator inserted between list elements.

Only strings are allowed in the list (not numbers or nested lists).

'''



list1 = ["Hi Suyash", "How are you","?"]

chars = ' '.join(list1)

print(chars)


# nested_list = ["Hi Krishna ",["How are you Krishna "],"I hope you are fine "]

# chars = ''.join(nested_list)

print(''.join(list1))      # No spaces
print(', '.join(list1))    # Adds commas
print(' | '.join(list1))   # Adds pipe symbol
