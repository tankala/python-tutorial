number = int(input("Please enter a number for which you want multiplication table: "))

multiplier = 1
while multiplier <= 10:
    mutliplied_value = number * multiplier
    # print(str(number) + " x " + str(multiplier) + " = " + str(mutliplied_value))
    print(f"{number} x {multiplier} = {mutliplied_value}")
    multiplier += 1