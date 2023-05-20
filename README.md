# Calculator
Calculator in Python


This Python script provides an advanced calculator that performs multiple mathematical operations. The implemented operations include addition, subtraction, multiplication, division, exponentiation, square root calculation, factorial calculation, and natural logarithm calculation. In addition, trigonometric functions like sine, cosine, and tangent are also implemented.

The user interface is command-line based. The program continuously asks the user to select an operation from a menu, then inputs the numbers on which the operation should be performed. After performing the operation, the program prints the result and again prompts the user to choose another operation. This cycle continues until the program is manually stopped.

1 - Addition: The add(x, y) function takes two arguments and returns their sum.
2 - Subtraction: The subtract(x, y) function subtracts the second number from the first one.
3 - Multiplication: The multiply(x, y) function returns the product of the two numbers.
4 - Division: The divide(x, y) function divides the first number by the second one. It also includes a condition to check if the denominator is zero to avoid a division by zero error.
5 - Exponentiation: The power(x, y) function calculates the first number raised to the power of the second number.
6 - Square Root: The sqrt(x) function calculates the square root of a number. For negative inputs, it returns a complex number using the cmath module.
7 - Factorial: The factorial(x) function calculates the factorial of a non-negative integer.
8 - Natural Logarithm: The log(x) function calculates the natural logarithm of a positive number.
9 - Sine: The sin(x) function calculates the sine of a number (the input is considered to be in degrees).
10 - Cosine: The cos(x) function calculates the cosine of a number (the input is considered to be in degrees).
11 - Tangent: The tan(x) function calculates the tangent of a number (the input is considered to be in degrees).

The calculator's functions handle different types of errors, such as division by zero, taking the square root of a negative number, or finding the factorial of a negative number. In each of these cases, the function will return an appropriate error message.
