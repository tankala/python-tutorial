age = int(input("Enter your Age. I will tell you for how many years you will get licence: "))

if age < 16:
    print("Sorry! You are not eligible for Driving Licence")
elif age < 30: # age >=16 and age < 30
    license_duration = 40 - age
    print("You will get licence for next " + str(license_duration) + " years")
elif age < 50: # age >=30 and age < 50
    print("You will get licence for next 10 years")
elif age <= 55: # age >=50 and age <= 55
    license_duration = 60 - age
    print("You will get licence for next " + str(license_duration) + " years")
else: # age > 55
    print("You will get licence for next 5 years")