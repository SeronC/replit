class Student():
  name = None
  subjects = None

  def __init__(self, name, subjects):
    self.name = name
    self.subjects = subjects

Rayyan = Student("Rayyan", "Further Maths, Maths, Physics")
print(Rayyan.name)
print(Rayyan.subjects)

Rayyan.subjects = "Chess"
print(Rayyan.subjects)
Classroom = []
Classroom.append(Rayyan)
print(Classroom[0].name)
print(Classroom[0].subjects)

print(Classroom[0].name, "studies", Classroom[0].subjects)
