from sklearn import svm

def addition(x, y):
    total = x + y
    return total

def subtraction(x, y):
    total = x - y
    return total

def division(x, y):
    total = x / y
    return total

def multiplication(x, y):
    total = x * y
    return total

def main():
    num1 = float(input("First Number:"))
    num2 = float(input("Second Number:"))
    operator = input("Operator:")
    
    if num1 < 0:
        print("First number cannot be negative.")
    elif num2 < 0:
        print("Second number cannot be negative.")
    elif operator == "+":
        total = addition(num1, num2)
        print("Total = ", total)
    elif operator == "-":
        total = subtraction(num1, num2)
        print("Total = ", total)
    elif operator == "*":
        total = multiplication(num1, num2)
        print("Total = ", total)
    elif operator == "/":
        total = division(num1, num2)
        print("Total = ", total)
    else:
        print("Invalid operator")

main()
