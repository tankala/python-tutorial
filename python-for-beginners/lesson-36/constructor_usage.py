from Human import Human

human1 = Human("Ashok", 34)
human2 = Human("Viswanadha Gupta", 65)
print(human1.name)
print(human2.name)

human1.age = 35
print(human1.age)

human1.walk()
human2.walk()