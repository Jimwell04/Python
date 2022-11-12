# Conditional in Python

age = int(input("Input your age: "))

if age >= 18 and age <= 50:
	print("You are Welcome")
elif age > 50:
	print("Sorry you are senior get out")
else:
	access = input("You have special access? ")
	if access == "Yes" or access == "yes":
		print("You are Welcome")
	else:
		print("You are minor get out!!!")
	
if not age >=  18:
	print("You are not 18+")
else:
	print("you are 18+")
