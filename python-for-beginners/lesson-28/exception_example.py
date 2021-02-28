try:
    number = int(input("Please give me a number: "))
    print("You have entered " + str(number))
except ValueError:
    print("Invalid input")