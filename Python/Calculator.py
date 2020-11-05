def doMath(a, b, function):
    if function == 1:
        return str(a + b)
    elif function == 2:
        return str(a - b)
    elif function == 3:
        return str(a * b)
    elif function == 4:
        return str(round(a / b, 2))
    else:
        return str(a % b)

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

print("Sum : " + doMath(a,b,1))
print("Difference : " + doMath(a,b,2))
print("Product : " + doMath(a,b,3))
print("Quotient : " + doMath(a,b,4))
print("Modulo : " + doMath(a,b,5))
