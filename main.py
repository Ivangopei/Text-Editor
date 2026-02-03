# Code written by: Ivan Gopei

import math
import random
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve, sympify, SympifyError


# --- BASIC OPERATIONS ---
# Sum of 2 numbers
def summation(*num):
    for i in num:  
        total += i
    return total

# Subtraction of the 2 numbers
def subtract(*num):
    for i in num:
        total += -i
    return total

# Division of 2 numbers
def div(*num):
    for i in num:
        total += -i
    return total

# Multiplication of 2 numbers
def mult(*num):
    for i in num:
        total *= num
    return total

# Percentage
def per(perc, num):
    new = perc / 100
    total = new * num
    return total


# --- POWER & ROOTS ---
# Square root of a digit
def root(num):
    total = math.sqrt(num)
    return total

# Digit to any power
def power(num, power):
    total = math.pow(num, power)
    return(total)


# --- SCIENTIFIC FUNCTIONS ---
# Sin of an angle (degree or a radian)
def sin(num):
    total = math.sin(num)
    return total

# Cos of an angle (degree or a radian)
def cos(num):
    total = math.cos(num)
    return total

# Tan of an angle (degree or a radian)
def tan(num):
    total = math.tan(num)
    return total

# Arcsin of an angle (degree or a radian)
def asin(num):
    total = math.asin(num)
    return total

# Arccos of an angle (degree or a radian)
def acos(num):
    total = math.acos(num)
    return total

# Arctan of an angle (degree or a radian)
def atan(num):
    total = math.atan(num)
    return total


# --- ALGEBRA STYLE ---
# Absolute value
def absol(num):
    total = abs(num)
    return total

# Factorials
def fact(num):
    total = math.factorial(num)
    return total

# Mod / remainder
def remain(num):
    total = math.factorial(num)
    return total

# Random numbers
def rand():
    total = random()
    return total


# --- ADVANCED (GRAPHING / CAS CALCULATORS) ---
# Solve equation
def eq():
    # Making x and y being defined as a variables in the equation
    x = symbols('x')

    # Lets the user to type the equation
    print("Enter an equation to solve for x (e.g. 2*x + 5 = 15):")
    user_input = input("> ")

    # Check is the "=" sign is present in the equation
    if '=' not in user_input:
        print("Error: The equation must have '=' sign") 
        return None 

    try:
        # Split the equation in 2 halves
        left, right = user_input.split('=')

        # Creates a math objects from the strings
        left_eq = sympify(left)
        right_eq = sympify(right)

        # Create the equation glueing two sides that we separated from the user's input before
        equation = Eq(left_eq, right_eq)

        # Solve the equation for x
        solution = solve(equation, x)
        return solution
    
    # The exception is thrown if the user didn't type the equation correctly (e.g. x = y = z)
    except ValueError:
        print("Error: Please check your format. Use exactly one '=' sign.")
        return None
    
    # The exception is thrown if the user didn't type the equation correctly (Bad -> x = y = z)
    except SympifyError:
        print("Error: Invalid syntax. Make sure to use '*' for multiplication (Bad -> 2 + * 5)")
        return None
    
    # The exception is thrown if the user did anything else incorrectly (like Division by Zero)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


# Graph functions
def graphing():
    print("Enter coordinates below for both x-axis and y-axis. "
    "**NOTE**: X should contain the same amount of values as Y and vice versa")

    while True:
        user_input_x = input("Enter coordinates for X separated by space: ")
        user_input_y = input("Enter coordinates for Y separated by space: ")

        x = [float(i) for i in user_input_x.split()]
        y = [float(i) for i in user_input_y.split()]

        if len(x) != len(y):
            print(f"Error! You entered {len(user_input_x)} Xs and {len(user_input_y)} Ys.")
            x = []
            y = []
            continue
        else:
            break

    plt.plot(x, y, c="red", linewidth=2, label="Line 1", marker='o')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Graph")
    plt.legend()
    plt.show()



# Derivatives & integrals
def 
# Matrices & vectors
def
# Complex numbers
def