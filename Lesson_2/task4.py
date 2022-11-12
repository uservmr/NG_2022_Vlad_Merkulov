number = int(input("Enter a number to calculate factorial: ")) 
factorial=1 
for number in range(2,number+1):
    factorial=factorial*number
print("Factorial", number,"=",factorial)