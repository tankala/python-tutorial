# file = open("readme1.txt", "w")
# file.write("line thirteen")
# file.close()
with open("readme1.txt", "w") as file:
    file.write("line one")
    print(file.closed)

print(file.closed)