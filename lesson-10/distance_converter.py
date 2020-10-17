# User input
distance_in_miles = input("Give me distance in miles. I will tell you how many kms it is: ")
# Type Coversion
distance_in_miles = float(distance_in_miles)
# Multiply with number to convert into required unit
distance_in_kms = distance_in_miles * 1.6
# Print
print(distance_in_kms)