# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

print("Greetings, I am CALCULORD-2099")
print("I am summoned, so I will flex on some integers for you")
print("Would you like to add, subtract, multiply or divide today?")

userpick = input("Your choice: ")

if userpick == "add":
	print("Enter your first number.")
	add1 = input(" ")
	print("Enter your second now.")
	add2 = input(" ")
	add1 = int(add1)
	add2 = int(add2)
	addition_total = int(add1 + add2)
	print("Your final sum is: " + str(addition_total))
if userpick == "subtract":
	print("Enter your first number.")
	sub1 = input(" ")
	print("Enter your second now.")
	sub2 = input(" ")
	sub1 = int(sub1)
	sub2 = int(sub2)
	sub_total = int(sub1 - sub2)
	print("Your final answer is: " + str(sub_total))
if userpick == "multiply":
	print("Enter your first number.")
	mult1 = input(" ")
	print("Enter your second now.")
	mult2 = input(" ")
	mult1= int(mult1)
	mult2 = int(mult2)
	mult_total = int(add1 * add2)
	print("Your final sum is: " + str(mult_total))
if userpick == "divide":
	print("Enter your first number.")
	divi1 = input(" ")
	print("Enter your second now.")
	divi2 = input(" ")
	divi1 = int(divi1)
	divi2 = int(divi2)
	divi_total = int(divi1 + divi2)
	print("Your final sum is: " + str(divi_total))
print("CALCULORD-2099 WISHES YOU LUCK IN LIFE, FAREWELL")
