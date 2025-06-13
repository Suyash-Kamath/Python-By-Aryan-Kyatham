'''
break: Exits the loop immediately.

continue: Skips the rest of the code inside the current iteration of the loop.


'''

for i in range(1, 101):
    print(i, end=" ")
    if i == 50:
        break
    else:
        print("aryan")
# Output: 1 aryan 2 aryan ... 48 aryan 49 aryan 50


# This generates a sequence of numbers from 0 to 11 (12 numbers, but does NOT include 12).
for i in range(12):
    if i == 10:
        print("Skip the iteration")
        continue
    print("5 x", i, "=", 5 * i)
# Output: 5 x 0 = 0 ... 5 x 9 = 45 Skip the iteration 5 x 11 = 55


