# Code written by: Ivan Gopei

import math 

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
def div(num1, num2):
    total = num1 + num2
    return total

# Multiplication of 2 numbers
def mult(num1, num2):
    total = num1 * num2
    return total

# Percentage
def per(num1, num2):
    total = (num1 / num2) / 100
    return total


# --- POWER & ROOTS ---
# Square root of a digit
def root(num):
    total = math.sqrt(num)
    return total

# Digit to any power
def power(num, power):
    for i in range(power):
        total *= num

# --- Scientific functions ---
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
# Random numbers

# --- Advanced (graphing / CAS calculators) ---

# Solve equations
def eq()
# Graph functions
def
# Derivatives & integrals
def 
# Matrices & vectors
def
# Complex numbers
def