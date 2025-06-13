# A for loop in Python iterates over a sequence of iterable objects, such as strings, lists, tuples, sets, and dictionaries.

name = "Suyash"
for i in name:
    print(i,end=", ")


color= ["red","green","blue"]

for i in color:
    print(i)
    for col in i:
        print(col)

# , the print() function adds a new line after every output.


for k in range(1, 200):
    print(k)  # Output: Numbers from 1 to 199


for k in range(2, 12, 2):
    print(k)  # Output: 2, 4, 6, 8, 10



# A while loop repeatedly executes a block of code as long as a condition is True.
count = 5
while count > 0:
    print(count)
    count -= 1
else:
    print("I am inside else")


'''

🔁 What is a Do-While Loop?



A do-while loop always runs at least once — because it executes the loop body first and then checks the condition after.


🐍 Python Does Not Have a do-while Loop
But we can simulate it using a while True: loop and a break statement.


'''

# ✅ Python Equivalent (Simulated do-while):

condition = False
while True:
    # loop body
    print("This will always print at least once")

    # condition check
    if not condition:
        print("Condition is False")
        break


while True:
    user_input = input("Enter something (type 'exit' to stop): ")
    if user_input == "exit":
        break
    print("You entered:", user_input)

