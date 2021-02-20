layer_count = int(input("Please give me how many layers equilateral triangle you want: "))

for layer_position in range(1, layer_count+1):
    row = ""
    for space_index in range(layer_count - layer_position):
        row += " "
    for index in range(layer_position):
        row += str(layer_position)
    for index in range(layer_position-1):
        row += str(layer_position)
    print(row)