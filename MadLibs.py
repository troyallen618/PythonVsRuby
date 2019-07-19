def Left():
	print("The "+Noun1+ " turns the corner and sees another group of " + PluralNoun1 + " and get captured.\n THE END")
def Right():
	print("The "+Noun1+ " runs into a " + Adjective1 +" "+Noun2+" and a "+ Adjective2+" "+Noun3+" who help fight off the "+PluralNoun1+". \n THE END")

print ("Welcome to Troy's Mad Libs Adventure!")


Noun1 = input("Enter a singular noun: ")
Noun2 = input("Enter another singular noun: ")
Noun3 = input("OK. This is the last singular noun you will have to input: ")
PluralNoun1 = input("Now, can you enter a plural noun: ")
Adjective1 = input("Please enter an adjective: ") 
Adjective2 = input("One more adjective please: ")
Adjective3 = input("And another adjective: ")
Direction1 = input("Enter Left or Right: ").upper()


print("One day a " + Noun1 + " was being chased by a group of " + Adjective3 + " " + PluralNoun1 + ".")
input('PRESS ENTER TO CONTINUE ')
print("The " + Noun1 + " ran to an intersection and decided to go " + Direction1 + ".")
input('PRESS ENTER TO CONTINUE ')
if Direction1 == "LEFT":
	Left()
else:
	Right()	
