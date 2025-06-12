'''
if: Basic conditional.
if-else: Conditional with alternative execution.
if-else-elif: Multiple conditions.
Nested if-else-elif: Conditions within conditions.

'''

iphonePrice = 60000
budget = 20000
if budget < iphonePrice:
    print("Kamao bsdk!")
else:
    print("lele bhai")


num = 0
if num < 0:
    print("number is negative")
elif num == 0:
    print("number is zero")
else:
    print("number is positive")


num = 18
if num < 0:
    print("Number is negative")
elif num > 0:
    if num <= 10:
        print("number is between 1-10")
    elif num > 10 and num <= 20:
        print("number is between 11-20")
    else:
        print("number is greater than 20")
else:
    print("number is zero")

