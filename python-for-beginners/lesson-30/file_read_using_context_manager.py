with open("readme.txt", "r") as file:
    print(file.read())
    print(file.closed)

print(file.closed)