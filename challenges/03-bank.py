print("Welcome to ChaseDaMoney bank.")
print("Have a nice day!")

## Create a prompt and make three methods - withdraw, deposit and check_balance

print("Bloody knobber you be? Well, slag. \n Ye finna withdraw, deposit or check_balance")
print("+++ withdraw +++ deposit +++ check_balance +++")
print("you may only pick one lol \n")

choice = input("Go on then... \n")

import random
import sys

funds = random.randint(-924,155)


def withdraw():
	getmoney = input("How much ya takin' out? \n")
	getmoney = int(getmoney)
	newbalance = funds - getmoney
	print("Oh..  Now you have " + str(newbalance) + "dollars. \n ok.")

def deposit():
	print("and you really want to deposit?  Ok..")
	putmoney = input("How much you puttin' in, big guy? \n")
	putmoney = int(putmoney)
	newbalance = funds + putmoney
	print("Yes, your new balance is indeed "+ str(newbalance))

def check_balance():
	print("It appears that you have " + str(funds) + " dollars.  Shame.")
	print("And that's how it went down. Goodbye")

if choice == "deposit":
	deposit()
	print("Thanks bye")
elif choice == "withdraw":
	withdraw()
	print("Ok cool. get it, ha")
elif choice == "check_balance":
	check_balance()
else:
	print("SORRY I DONT UNDERSTAND YOU")
	sys.exit

print("Anything else you need today?")
lastthing = input(": ")
if lastthing == "yes":
	print("deposit, withdraw or gtfo?")
	anotherone = input(": ")
	if anotherone == "deposit":
		deposit()
	elif anotherone == "withdraw":
		withdraw()
	else:
		print("YEAH OK KID. NICE ONE")
		sys.exit
if lastthing != "yes":
	print("PFFFFFTTTT")
	sys.exit

