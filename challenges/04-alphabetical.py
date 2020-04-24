# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

# cutit takes a string, seperates into characters and returns them in a list
def cutit(word):
		return [char for char in word]

#user inputs string
chaos = input("Gimme a string, big boy. \n")
# let's get choppin' boys
choppy = cutit(chaos)
#  a silent sorting affair
choppy.sort()
# I guess this is what y'all came to see, right?
print(choppy)
