file = open("readme.txt", "r")
# print(file.read())
# Read 10 characters
# print(file.read(10))
# print(file.read(10))
# Read line
# print(file.readline())
line = file.readline()
while line:
    print(line)
    line = file.readline()
print(file.name)
file.close()