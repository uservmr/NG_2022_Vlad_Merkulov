number = int(input("Enter a number to calculate factorial: ")) 
factorial=1 
for n in range(2,number+1):
    factorial=factorial*n
print("Factorial", number,"=",factorial)