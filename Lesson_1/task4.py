import math
print("Enter the coefficients for the equation(a,b,c): ")
print("=====================")
print("Quadratic equation(ax^2 + bx + c = 0):")
print("=====================")
a = float(input("Coefficient a = "))
b = float(input("Coefficient b = "))
c = float(input("Coefficient c = "))
print("=====================")
D = b ** 2 - 4 * a * c
print("Discriminant D =", D)
print("=====================")
if (D > 0):
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print("x1 =", x1)
    print("x2 =", x2)
elif (D == 0):
    x = -b / (2 * a)
    print("x = ", x)
else:
    print("No roots")
print("=====================")    