def add(first_number, second_number):
    return first_number + second_number

def subtract(first_number, second_number):
    return first_number - second_number

def multiply(first_number, second_number):
    return first_number * second_number

def division(first_number, second_number):
    return first_number / second_number

def modulus(first_number, second_number):
    return first_number % second_number

def invalid():
    return "Invalid operator"

def calculate(first_number, operator, second_number):
    if operator == "+":
        result = add(first_number, second_number)
    elif operator == "-":
        result = subtract(first_number, second_number)
    elif operator == "*":
        result = multiply(first_number, second_number)
    elif operator == "/":
        result = division(first_number, second_number)
    elif operator == "%":
        result = modulus(first_number, second_number)
    else:
        result = invalid()
    
    print(result)

first_number = float(input("Please Enter first number: "))
operator = input("Please Enter operator: ")
second_number = float(input("Please Enter second number: "))
calculate(first_number, operator, second_number)