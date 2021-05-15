# AND truth table
# 0101
# 0011
# 0001
first_number = 5
second_number = 6
# 5 & 6 = 4
# 5      = 00000101
# 6      = 00000110
# Result = 00000100
print("AND Operator result: ")
print(first_number & second_number)

# OR truth table
# 0101
# 0011
# 0111
# 5 | 6 = 7
# 5      = 00000101
# 6      = 00000110
# Result = 00000111
print("OR Operator result: ")
print(first_number | second_number)

# XOR truth table
# 0101
# 0011
# 0110
# 5 ^ 6 = 3
# 5      = 00000101
# 6      = 00000110
# Result = 00000011
print("XOR Operator result: ")
print(first_number ^ second_number)

# not truth table
# 01
# 10
# ~n = -(n+1)
# ~6 = -7
print("NOT operator result: ")
print(~second_number)

# Left shift
# 5    = 00000101
# 5<<2 = 00010100 = 20
print("Left Shift: ")
print(first_number << 2)

# Right shift
# 5    = 00000101
# 5>>2 = 00000001 = 1
print("Right shift: ")
print(first_number >> 2)