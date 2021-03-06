with open("user_input.txt", "r+") as file:
    user_input = input("Please give some text to store(Type STOP to stop this program): ")
    while user_input != "STOP":
        file.write(user_input + "\n")
        user_input = input("Please give some text to store(Type STOP to stop this program): ")
    file.seek(0)
    print("File name: " + file.name)
    print("-------------------------")
    print(file.read())
    print("-------------------------")