class Human:
    def __init__(self, name):
        self.__name = name

    def info(self):
        print("Name -", self.__name)

    def setName(self, newName):
        self.__name = newName


class Student(Human):
    def __init__(self, name, scoolName):
        self.__scName = scoolName
        super().__init__(name)

    def info(self):
        print("Student :")
        super().info()
        print("Scool : ", self.__scName)



h = Human("Vasya")
# print(h.__name)
h.info()
h.setName("Vasya III")
h.info()


s = Student("Petya", "IT STEP")
s.info()