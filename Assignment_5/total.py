import sys

count = len(sys.argv)
total = 0
while count > 1:
    count -= 1
    total += float(sys.argv[count])

try:
    avg = total / (len(sys.argv)-1)
except:
    print("No arguments were passed")
else:
    print("Average is",avg)
    
print("Total is", total)

