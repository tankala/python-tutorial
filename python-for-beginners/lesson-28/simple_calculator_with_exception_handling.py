try:
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
except ValueError:
    print("Invalid input number")
except ZeroDivisionError:
    print("Zero Division is not possible")
# except:
#     print("Something went wrong")