number = int(input("Please give me a number I will tell you is it prime number or not: "))

divisor = 2
while divisor < number:
    reminder = number % divisor
    if reminder == 0:
        break
    divisor += 1

if divisor == number:
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")