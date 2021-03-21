from weight_converter import *

weight = input("Give me Weight: ")
choice = input("From which unit to which unit you want to convert? Type 1 for Kgs to Pounds, 2 for Pounds to Kgs: ")

if choice == '1':
    print(kgs_to_pounds(weight))
elif choice == '2':
    print(pounds_to_kgs(weight))
else:
    print(f"Wrong Choice.\nA Simple coversion fact about Kgs to Pounds.\n1kg = {kgs_to_pounds_number} lbs")