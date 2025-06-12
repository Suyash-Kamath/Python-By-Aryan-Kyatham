# Strings are sequences of textual data enclosed within single or double quotation marks.

# Accessing Character


name = "Suyash"

print(name[0])
print(name[1])

# Strings can be accessed like arrays with indices starting from 0.

'''
String Slicing
Slicing refers to extracting parts of a string using indices.

'''

fruit="Mango"

len1=len(fruit)

print("Mango is a ",len1,"letter word")

# String as an Array

# Strings are sequences of characters.

pie = "Apple Pie"

print(pie[:5])
print(pie[6])
print(pie[-1]) # peeche se dekho

print(pie[-2])
print(pie[-3])
print(pie[:-2])

'''

Fizz Buzz Type Problem Generator

✅ What it does:
This defines a list of tuples, where:

Each tuple has:

a number (divisor)

a word (to print if divisible)


This is the heart of the program. Let’s break it:

for divisor, word in conditions → Loop through each tuple.

if i % divisor == 0 → Check if i is divisible by divisor.

word → Get the corresponding word if divisible.

"".join(...) → Combine all matching words into a single string.

📌 Example:
Let’s say i = 15:

Divisible by 3 → "fizz"

Divisible by 5 → "buzz"

Final output → "fizzbuzz"


'''

conditions = [
 (3, "fizz"),
(5, "buzz"),
(7, "bizz"),
(9, "bazz")
]

for i in range(1,100):
    output = "".join(word for divisor,word in conditions if i%divisor==0)
    if not output:
        output = str(i)
    print(output,i)



# --------------------------------------------------------------------------------------------

str =  "AbcdEfghIJ"
print('Converts the string to uppercase.',str.upper())
print('Converts the string to lowercase.',str.lower())

str1 = "   Hi Suyash   "
print(str1.strip())
# Removes whitespace before and after the string. output is "Hi Suyash"

str2 = "Hi Suyash!?&%!!!!!"
print('rstrip(): Removes trailing characters.',str2.rstrip("!?"))
# The function rstrip(chars) removes any characters that match those in chars — but only from the right end (the end of the string).
# “Keep removing ! or ? from the end of the string until you hit a character that's not ! or ?.”

# rstrip("xyz") removes all occurrences of any of x, y, or z from the end of the string, until it hits a character that is not in that group.

str1.replace("Suyash","Krishna")
print(str1)

'''
 In Python, strings are immutable.
That means: string methods like .replace() do not change the original string. They return a new modified string.

str1 = "Hi Suyash"
str1.replace("Suyash", "Krishna")  # returns: "Hi Krishna"
print(str1)                        # still prints: "Hi Suyash"


 What is Immutability?
In Python, immutable means:

Once a value is created, it cannot be changed in-place.

So, when you "change" a string using methods like .replace(), .upper(), .lower(), etc., Python actually creates a new string in memory.

To store the new string:
str1 = str1.replace("Suyash", "Krishna")

Now str1 points to the new string:
str1 ───► "Hi Krishna"   (at 0xB002)

The original "Hi Suyash" is still in memory (temporarily), but Python might delete it later using garbage collection.

'''

str3 = "Hi Suyash"
str4 = str3.replace("Suyash","Krishna")
print(str4)





# split(): Splits the string into a list based on a separator
str2 = "Silver spoon"
print(str2.split(" "))  
# Output: ['Silver', 'spoon']

#  capitalize(): Capitalizes only the first character of the string
text = "hello world"
print(text.capitalize())  
# Output: "Hello world"

#  center(width): Places the string in the center of a given width
text = "hello"
print(text.center(11))  
# Output: "   hello   "
# Explanation: Pads the text with spaces on both sides so it sits centered in 11 characters.


# count(): Counts how many times a character or substring appears
text = "abracadabra"
print(text.count("a"))  
# Output: 5


# endswith(): Checks if the string ends with a certain value
text = "Hello world!"
print(text.endswith("!"))  
# Output: True
print(text.endswith("world"))  
# Output: False


# find(): Returns the index of the first occurrence of a substring
text = "He's name is Aryan and he is good"
print(text.find("is"))  
# Output: 10  (1st "is" in "is Aryan")

print(text.find("Daniel"))  
# Output: -1 (Not found)

#  find() returns -1 if the substring is not found.



# isalnum(): Returns True if all characters are letters or numbers
print("Hello123".isalnum())  
# Output: True

print("Hello 123".isalnum())  
# Output: False (because of space)

print("123443".isalnum())
# True


#  islower(): Returns True if all alphabetic characters are lowercase
print("hello".islower())  
# Output: True

print("Hello".islower())  
# Output: False


# isprintable(): Checks if all characters in the string are printable
print("Hello123!".isprintable())  
# Output: True

print("Hello\nWorld".isprintable())  
# Output: False (newline character is not printable)


#  isspace(): Checks if the string only contains whitespace
print("   ".isspace())  
# Output: True

print("  a  ".isspace())  
# Output: False


# istitle(): True if each word starts with an uppercase letter
print("This Is Title Case".istitle())  
# Output: True

print("This is not Title Case".istitle())  
# Output: False


# isupper(): True if all alphabetic characters are uppercase
print("HELLO".isupper())  
# Output: True

print("Hello".isupper())  
# Output: False


