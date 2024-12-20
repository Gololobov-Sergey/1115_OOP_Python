import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 30
        self.progress = 10
        self.alive = True
        self.energy = 50

    def study(self):
        print("Я пішов навчатися")
        self.progress += 1
        self.energy -= 1
        self.gladness -= 1

    def sleep(self):
        print("Я пішов спати")
        self.energy += 2
        self.gladness += 1

    def chill(self):
        print("Я пішов з друзяками гулять")
        self.energy -= 1
        self.progress -= 1
        self.gladness += 2



    def info(self):
        print(f"На сьогодні {self.name} має:")
        print(f"Задоволення : {self.gladness}")
        print(f"Знання      : {self.progress}")
        print(f"Енергія     : {self.energy}")


    def is_alive(self):
        if self.progress < 0:
            print(f"В мене в голові сміття, життя не має сенсу")
            self.alive = False
        if self.gladness < 0:
            print(f"В мене дипресія")
            self.alive = False
        if self.progress > 100:
            print(f"Я такий розумний, що достроково закінчив МКА ШАГ!")
            self.alive = False
        if self.energy < 0:
            print(f"Я зовсім знесилений")
            self.alive = False

    def live(self, day):
        print(f"День №{day} з життя {self.name}")
        print("-"*30)
        rnd = random.randint(1,3)
        if rnd == 1:
            self.study()
        elif rnd == 2:
            self.chill()
        elif rnd == 3:
            self.sleep()
        #

        self.info()
        self.is_alive()
        print()


st = Student("Вася")
for d in range(1, 366):
    if st.alive == False:
        break
    st.live(d)
