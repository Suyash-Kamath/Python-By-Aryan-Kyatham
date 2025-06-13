# A function is a block of code that performs a specific task whenever it is called. Functions help make code neater and more reusable.

# Built-in Functions: min(), max(), len(), sum(), type(), tuple(), list(), set(), print(), range(), dict()

# User-Defined Functions: Functions created to perform specific tasks as per the needs of the user.

def greet(fname, lname):
    print("Hello", fname, lname)

greet("Suyash", "Kamath")


# Function Arguments

# Default Arguments: Provide default values for function parameters.

def greet(fname, mname="Gurunath", lname="sharma"):
    print("Hello", fname, mname, lname)

greet("Rohit")  # Output: Hello Rohit Gurunath Sharma


# Keyword Arguments: Provide values in a key-value format, allowing you to skip the order of arguments.

def greet(fname, mname, lname):
    print("Hello", fname, mname, lname)

greet(mname="Peter", lname="wesker", fname="Jaden")
# Output: Hello Jaden Peter Wesker

# Required Arguments: All required arguments must be provided.

# This will raise an error because 'lname' is missing
# greet("suyash", "bhai")
# Output: TypeError: greet() missing 1 required positional argument: 'lname'


# Variable-Length Arguments: Allow passing more arguments than defined.
# Arbitrary Arguments:
def greet(*names):
    print(names)
    print("Hello",names[0],names[1],names[2])

greet("Suyash","Bhai","Kamath")
# 🟡 *names in Python:
# The asterisk * before a parameter in a function like this:def greet(*names): Means that the function can take any number of arguments, and they will be collected into a tuple named names.


# Keyword Arguments:

def greet(**names):
    print(names["fname"], names["mname"], names["lname"])

greet(fname="Suyash", mname="Ram", lname="Krishna")

# What is **names? def greet(**names):
# The double asterisk ** allows your function to accept any number of keyword arguments.
# These keyword arguments are stored in a dictionary named names.

'''

🧠 Example:
When you call:

greet(fname="Aryan", mname="Zayn", lname="Khalid")

The names variable becomes:
{
    "fname": "Aryan",
    "mname": "Zayn",
    "lname": "Khalid"
}




| Syntax     | Meaning                                                         |
| ---------- | --------------------------------------------------------------- |
| `*args`    | Accepts any number of **positional arguments** as a **tuple**   |
| `**kwargs` | Accepts any number of **keyword arguments** as a **dictionary** |


'''

def example(*args, **kwargs):
    print(args)   # Tuple of values
    print(kwargs) # Dictionary of key-value pairs

example(1, 2, 3, name="John", age=30)


# Return Statement: Sends a value back from a function to where it was called.

def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8