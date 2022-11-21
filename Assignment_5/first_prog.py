#this line takes input from the user
number = input("Enter a number: ")

#changes the given number into integer
number = int(number)

#prints the given number
print("The numbered entered was", number)

#checks whether the number is odd or even
if (number % 2) == 0:
	print("That is an even number")
else:
	print("That is an odd number")

#checks whether the number is divisible by 10 or not
if (number%10) == 0:
      print("This number is divisible by 10")
else:
	print("This number is not divisible by 10")
	
