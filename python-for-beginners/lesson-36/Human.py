class Human:
    def walk(self):
        print(self.name + " is Walking")
    def talk(self):
        print("Talking")
    
    def __init__(self, name, age):
        self.name = name
        self.age = age