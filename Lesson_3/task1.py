def Addition(x, y):
   return x + y
def Subtraction(x, y):
   return x - y
def Multiplication(x, y):
   return x * y
def Division(x, y):
   return x / y
def Power(x, y):
   return x ** y
def SquareRoot(x):
    return x ** 0.5
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
print("==============================")
func = print("Select function: \nAddition(x1+x2) - 1\nSubtraction(x1-x2) - 2\nMultiplication(x1*x2) - 3\nDivision(x1/x2) - 4\nSquaring(x*x) - 5\nSquare Root(x**0.5) - 6\nCompletion of the program - 7")
print("==============================")
func = int(input("Choose a function:"))
if (func == 1):
   print("Answer:", Addition(number1, number2))
elif (func == 2):
   print("Answer", Subtraction(number1, number2))
elif (func == 3):
   print("Answer:", Multiplication(number1, number2))
elif (func == 4):
   print("Answer:", Division(number1, number2))
elif (func == 5):
   print("Answer:", Power(number1, number2))
elif (func == 6):
    print("Answer:", round(SquareRoot(number1),2))
elif (func == 7):
    exit(1)
else:
   print("Incorrect input")

