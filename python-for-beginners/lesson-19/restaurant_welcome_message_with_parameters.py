def welcome_message(customer_name):
    print("Hi " + customer_name)
    print("Welcome to Our Restaurant")
    print("We serve both Asian and Western Cuisine")

def thank_you_message(customer_name, title = ""):
    print("Thank you for choosing us " + title + customer_name)
    print("Please visit us soon")

husband_name = input("Please give your name Sir: ")
welcome_message(husband_name)

wife_name = input("Please give your name Madam: ")
welcome_message(wife_name)

kid_name = input("Please give your cute name: ")
welcome_message(kid_name)

thank_you_message(customer_name = husband_name, title = "Mr. ")
thank_you_message(wife_name, "Mrs. ")
thank_you_message(customer_name = kid_name)