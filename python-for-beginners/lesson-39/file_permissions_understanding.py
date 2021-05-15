# Read, Write, Execute
# 100
# 010
# 001
read_permission = 4
write_permission = 2
execute_permission = 1
user_permission = (read_permission|write_permission|execute_permission)
# print(user_permission)
user_permission = (read_permission|execute_permission)

if user_permission & write_permission:
    print("Have write permission")
else:
    print("No write permission")

if user_permission & read_permission:
    print("Have read permission")
else:
    print("No read permission")