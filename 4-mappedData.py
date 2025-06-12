'''
🔷 What is a Dictionary in Python?
A dictionary is a type of data structure in Python that stores data in the form of key-value pairs.

🔑 Key → like a label (must be unique)
📦 Value → the actual data (can be anything)


| Feature           | Why It's Useful                                                |
| ----------------- | -------------------------------------------------------------- |
| 🔍 Fast Lookup    | You can find a value quickly using a key                       |
| 🧭 Organized      | Good for **structured data** like user info, configs           |
| 🧠 Human-Readable | Clear and easy to understand                                   |
| 🔁 Flexible       | Values can be strings, numbers, lists, even other dictionaries |



A dictionary is a container for labeled data.

It stores key-value pairs.

Used when you want to name each piece of data clearly.

Very helpful for real-world structured data, like users, products, settings.

'''

dict1 = {
    "name":"Suyash",
    "age":20,
    "canCode":True
}

print(dict1["name"])

# Real World Use Cases
# User Profiles
user  = {
    "username":"Suyash Kamath",
    "email":"suyashkamath@gmail.com",
    "is_active" : True
}

# Storing JSON data from an API

weather = {
    "city": "Mumbai",
    "temperature": 32,
    "unit": "Celsius"
}

# Nested Dictionaries

student={
    "name": "Aryan",
       "grades": {
           "math": 90,
            "science": 88
             }
}

print(student["grades"]["math"])