# Quadratic Solver
# Written by Owen McKenney

import math

def solve(a, b, c):
    d = b ** 2 - 4 * a * c # this calculates the discriminant
    roots = []

    if d < 0: # if the discriminant is negative, there are no real roots
        roots = ["There are no", "real roots"]
    else:
        roots = [round((-b + math.sqrt(d)) / 2 * a, 2), round((-b - math.sqrt(d)) / 2 * a, 2)] # this line finds both roots and adds them to a list

    return roots

print("Enter the coefficients for ax^2 + bx + c = 0") # these lines get user input for a, b and c
a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))

r = solve(a, b, c)
print(r[0], r[1]) # this prints out the roots

