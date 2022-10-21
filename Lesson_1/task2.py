import math
func = int(input('Select function: \nAddition(x1+x2) - 1\nSubtraction(x1-x2) - 2\nMultiplication(x1*x2) - 3\nDivision(x1/x2) - 4\nSquaring(x*x) - 5\nSquare Root(x**0.5) - 6\nCompletion of the program - 7\n'))
print("==============================")
if (func == 1):
    x1 = int(input('Enter the first number: '))
    x2 = int(input('Enter the second number: '))
    print("==============================")
    rezult = x1 + x2
elif (func == 2):
    x1 = int(input('Enter the first number: '))
    x2 = int(input('Enter the second number: '))
    print("==============================")
    rezult = x1 - x2
elif (func == 3):
    x1 = int(input('Enter the first number: '))
    x2 = int(input('Enter the second number: '))
    print("==============================")
    rezult = x1 * x2
elif (func == 4):
    x1 = int(input('Enter the first number: '))
    x2 = int(input('Enter the second number: '))
    print("==============================")
    rezult = float(x1 / x2)
elif (func == 5):
    x = int(input('Enter the number: '))
    print("==============================")
    rezult = x * x
elif (func == 6):
    x = int(input('Enter the number: '))
    print("==============================")
    sqrt = float(x ** (0.5))
    rezult = round(sqrt,2)
elif (func == 7):
    exit(1)
print('Answer: ', rezult)