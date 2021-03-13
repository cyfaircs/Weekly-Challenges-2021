number = input("Input a number to factor.")
number = int(number)
factors = []
for x in range (number, 0,-1):
#	print(x)
	x = int(x)
	remainder = (number%x) 
	remainder  = int(remainder)
#	print(remainder)
	if remainder == 0:
#		print("Wowie!")
		factors.append(x)
if number == 0:
		print("Zero is weird! Think of any number, and it's a factor!")
elif len(factors) == 2:
		print("{} is prime. Its only factors are {} and 1.".format(number,number))
else:
	print("The factors of {} are: {}".format(number,factors))