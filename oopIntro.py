class Person:
  __name = ""

  def __init__(self, name):
    self.__name = name

  def getPersonName(self):
    print(self.__name)

  def setter(self, name):
    self.__name = name

p1 = Person("John")
p1.getPersonName()
p1.setter("Rohit")
p1.getPersonName()
