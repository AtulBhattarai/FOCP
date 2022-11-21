from sys import argv

def average(values):
    """ Calculates the average of the given list. """
    total = 0;
    for n in values:        	# total the given values
        total += float(n)   	 
    return total/len(values)	# return calculated average

# initialisation statement
print("Welcome, utils module has been imported and initialised!")

if __name__ == "__main__":
    num = (argv[1:])
    print("Average is", average(num))
