first_number = float(input("Please Enter first number: "))
operator = input("Please Enter operator: ")
second_number = float(input("Please Enter second number: "))

if operator == "+":
    print(first_number + second_number)
elif operator == "-":
    print(first_number - second_number)
elif operator == "*":
    print(first_number * second_number)
elif operator == "/":
    print(first_number / second_number)
elif operator == "%":
    print(first_number % second_number)
else:
    print("Invalid operator")