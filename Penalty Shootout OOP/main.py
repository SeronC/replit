class footballer():
    name = None
    position = None
    number = None
    skillLevel = None

    def __init__(self, name, position, number, skillLevel):
        self.name = name
        self.position = position
        self.number = number
        self.skillLevel = skillLevel


footballer1 = footballer("Manraj", "GK", 99, 21)
#print(footballer1.name)
footballer2 = footballer("Mr Kloss", "CB", 6, 100)
#print(footballer2.name)

print(footballer2.name + " is taking a penalty against " + footballer1.name)
if footballer2.skillLevel > footballer1.skillLevel:
    print("GOAL!")
else:
    print("SAVED!")

myfootballers = []
