from weight_converter import *

weight = input("Give me weight: ")
choice = input("From which unit to which unit you want to convert? Type 1 for kgs to pounds, Type 2 for pounds to kgs: ")

if choice == '1':
    print(kgs_to_pounds(weight))
elif choice == '2':
    print(pounds_to_kgs(weight))
else:
    print(f"Wrong choice.\nA Simple conversion fact about kgs to pounds.\n1kg = {kgs_to_pounds_number} lbs")