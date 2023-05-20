import math
import cmath

def add(x, y):
    """This function adds two numbers"""
    return x + y

def subtract(x, y):
    """This function subtracts two numbers"""
    return x - y

def multiply(x, y):
    """This function multiplies two numbers"""
    return x * y

def divide(x, y):
    """This function divides two numbers"""
    if y == 0:
        return "Error! Division by zero is not allowed."
    else:
        return x / y

def power(x, y):
    """This function calculates the power of a number"""
    return x ** y

def sqrt(x):
    """This function calculates the square root of a number"""
    if x < 0:
        return cmath.sqrt(x)
    else:
        return math.sqrt(x)

def factorial(x):
    """This function calculates the factorial of a number"""
    if x < 0:
        return "Error! Factorial of a negative number doesn't exist."
    elif x == 0:
        return 1
    else:
        return math.factorial(x)

def log(x):
    """This function calculates the natural logarithm of a number"""
    if x <= 0:
        return "Error! Logarithm of zero or negative number is undefined."
    else:
        return math.log(x)

def sin(x):
    """This function calculates the sine of a number"""
    return math.sin(math.radians(x))

def cos(x):
    """This function calculates the cosine of a number"""
    return math.cos(math.radians(x))

def tan(x):
    """This function calculates the tangent of a number"""
    return math.tan(math.radians(x))

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Power")
print("6.Square Root")
print("7.Factorial")
print("8.Logarithm")
print("9.Sine")
print("10.Cosine")
print("11.Tangent")

while True:
    choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10/11): ")

    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            result = divide(num1, num2)
            if isinstance(result, str):
                print(result)
            else:
                print(num1, "/", num2, "=", result)
        elif choice == '5':
            print(num1, "raised to power", num2, "=", power(num1, num2))
    elif choice in ('6', '7', '8', '9', '10', '11'):
        num1 = float(input("Enter a number: "))

        if choice == '6':
            result = sqrt(num1)
            if isinstance(result, complex):
                print("Square root of", num1, "=", result)
            else:
                print("Square root of", num1, "=", result)
        elif choice == '7':
            result = factorial(num1)
            if isinstance(result, str):
                print(result)
            else:
                print("Factorial of", num1, "=", result)
        elif choice == '8':
            result = log(num1)
            if isinstance(result, str):
                print(result)
            else:
                print("Natural logarithm of", num1, "=", result)
        elif choice == '9':
            print("Sine of", num1, "=", sin(num1))
        elif choice == '10':
            print("Cosine of", num1, "=", cos(num1))
        elif choice == '11':
            print("Tangent of", num1, "=", tan(num1))
    else:
        print("Invalid Input")