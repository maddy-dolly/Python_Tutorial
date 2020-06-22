class User:
    name=""

    def __init__(self, name):
        self.name = name

    def printName(self):
        print("Name = " + self.name)

class Students(User):
    pass

brian = Students("Madhu")
brian.printName()

