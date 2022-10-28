x = int(input("Enter a number to calculate factorial: ")) 
factr=1 
for i in range(2,x+1):
    factr=factr*i
print("Factorial", x,"=",factr)