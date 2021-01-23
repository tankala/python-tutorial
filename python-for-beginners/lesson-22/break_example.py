login_attempts = 0
correct_pin = 1234

while login_attempts <= 3:
    pin = int(input("Please enter your ATM PIN: "))
    login_attempts += 1
    if pin == correct_pin:
        print("Login Successfull")
        break
    else:
        print("Wrong Pin. Please try Again")

if login_attempts > 3:
    print("Your Account is blocked")