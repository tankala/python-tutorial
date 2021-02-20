layer_count = int(input("Please give me how many layers right angle triangle you want: "))

for layer_position in range(1, layer_count+1):
    row = ""
    for index in range(layer_position):
        row += str(layer_position)
    print(row)