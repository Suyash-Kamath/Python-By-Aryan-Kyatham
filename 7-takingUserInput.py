x = int(input("Enter the Value of X: "))
y = int(input("Enter the Value of Y: "))

print(x+y)

# By Default it accepts input as string so Typecast when performing the numeric operations 


'''
 You're 100% Right:

 Yes — this is correct:
 input("Enter the Value of X:")

 always returns a string in Python. ✅

 so
 x = input("Enter the Value of X:")

 If you type 7, it's actually treated as the string "7".

 🔍 What happens when you do int(input(...))?

 You are doing this

 x = int("7")  # This works, because "7" is a valid integer in string form
So Python successfully converts the string "7" to the integer 7.


❌ But what if you enter "a"?

Then you're doing this 

x = int("a")  # ❌ FAIL: Python says "What is this? This is not a number!"


Python doesn't automatically assume you want the ASCII value of 'a'. The int() function is only designed to convert strings that look like numbers, like:

"8" ✅

"-5" ✅

"12" ✅

"3.14" ❌ (that’s a float, not int)

"a" ❌

'''