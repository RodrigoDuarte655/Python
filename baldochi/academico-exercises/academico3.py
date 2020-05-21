from abc import ABC, abstractclassmethod


class Person(ABC):
    def __init__(self, name, address, age, disciplineList):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__disciplineList = disciplineList

    def getName(self):
        return self.__name

    def getAddress(self):
        return self.__address

    def getAge(self):
        return self.__age

    def getDisciplineList(self):
        return self.__disciplineList

    def insertDiscipline(self, disc):
        self.__disciplineList.append(disc)

    @abstractclassmethod
    def printDescription(self):
        pass


class Professor(Person):
    def __init__(self, name, address, age, titulation, disciplineList):
        super().__init__(name, address, age, disciplineList)
        self.__titulation = titulation

    def getTitulation(self):
        return self.__titulation

    def printDescription(self):
        print('Name: {}'.format(self.getName()))
        print('Address: {}'.format(self.getAddress()))
        print('Age: {}'.format(self.getAge()))
        print('Titulation: {}'.format(self.getTitulation()))
        print('Taught Disciplines')
        disciplineList = self.getDisciplineList()
        for disc in disciplineList:
            print('Name: {} - Schedule hourly: {}'.format(disc.getDisciplineName(),
                                                          disc.getScheduleHourly()))


class Student(Person):
    def __init__(self, name, address, age, major, disciplineList):
        super().__init__(name, address, age, disciplineList)
        self.__major = major

    def getMajor(self):
        return self.__major

    def printDescription(self):
        print('Name: {}'.format(self.getName()))
        print('Address: {}'.format(self.getAddress()))
        print('Age: {}'.format(self.getAge()))
        print('Major: {}'.format(self.getMajor()))
        print('Taken Disciplines')
        disciplineList = self.getDisciplineList()
        for disc in disciplineList:
            print('Name: {} - Schedule hourly: {}'.format(disc.getDisciplineName(),
                                                          disc.getScheduleHourly()))


class Discipline():
    def __init__(self, disciplineName, scheduleHourly):
        self.__disciplineName = disciplineName
        self.__scheduleHourly = scheduleHourly

    def getDisciplineName(self):
        return self.__disciplineName

    def getScheduleHourly(self):
        return self.__scheduleHourly


subject1 = Discipline('Programming', 64)
subject2 = Discipline('Data Structures', 64)
subject3 = Discipline('Database', 64)

prof = Professor('John', 'Av.BPS, 1303', 33, 'doctor degree', [])
prof.insertDiscipline(subject1)
prof.insertDiscipline(subject2)

prof.printDescription()

print()

student = Professor('Rodrigo', 'Evaristo doctor', 229,
                    'doctor degree', [])
student.insertDiscipline(subject2)
student.insertDiscipline(subject3)

student.printDescription()

student.insertDiscipline(subject1)

print()

student.printDescription()
