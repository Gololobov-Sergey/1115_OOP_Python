class Student:
    print("Hi!")
    count_of_student = 0
    def __init__(self, name="No name", height=160, age=15):
        self.name = name
        self.height = height
        self.age = age
        Student.count_of_student += 1

    def addYear(self):
        if self.age < 100:
            self.age += 1

    def study(self):
        print("Я навчаюсь")

    # def info(self):
    #     print(f"Name    - {self.name}")
    #     print(f"Age     - {self.age}")
    #     print(f"Height  - {self.height}")

    def __str__(self):
        return f"Name    - {self.name}\n" + f"Age     - {self.age}\n" + f"Height  - {self.height}\n"

print(Student.count_of_student)

student1 = Student("Anton", 180)
# student1.info()
student1.addYear()
print(student1.count_of_student)
# student1.info()
print(student1)


# print(student1.name)
# print(student1.height)
# student1.height = 185
# print(student1.height)
# print(student1.age)
# student1.addYear()
# student1.addYear()
# student1.addYear()
# print(student1.age)
# student1.study()


student2 = Student("Ivan", 150)
print(student2.name)
print(student2.height)
print(student2.count_of_student)
#
# student3 = Student()
# print(student3.name)
# print(student3.height)
