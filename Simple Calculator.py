# Simple Calculator
try:
    num1 = float(input("Enter Your First Number: "))
    operator = input("input an operation (+, -. *, /):")
    num2 = float(input("Enter Your Second Number: "))
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        if num2 == 0:
            print("Cannot Divide By Zero!")
        else:   
            print(num1 / num2)
    else:
        print("Invalid Operation")
except ValueError:
    print("Numbers Only!")