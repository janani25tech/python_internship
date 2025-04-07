def calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b if b != 0 else "Error! Division by zero."
    elif operator == '%':
        return a % b if b != 0 else "Error! Modulo by zero."
    else:
        return "Invalid operator!"


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /, %): ")
print("Result:", calculator(num1, num2, op))
