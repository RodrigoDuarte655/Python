class Student():
    #pass
    def __init__(self):
        self.__name = "No name"
        self.__university = "No university"
        self.__age = 0

    #Mutator methods
    def setName(self, name):
        self.__name = name

    def setUniversity(self, university):
        self.__university = university

    def setAge(self, age):
        self.__age = age

    #Accessor methods
    def getName(self):
        return self.__name

    def getUniversity(self):
        return self.__university

    def getAge(self):
        return self.__age

    def __str__(self):
        return '{} is a {} year-old student at the {}.'.format(self.__name, self.__age, self.__university)

def main():
    print("Hello student!!!")

    newStudent = Student()
    newStudent.setName(input("Name: "))
    newStudent.setUniversity(input("University: "))
    newStudent.setAge(int(input("Age: ")))

    print()
    print("Student name: {}".format(newStudent.getName()))
    print("Student university: {}".format(newStudent.getUniversity()))
    print("Student age: {}".format(newStudent.getAge()))

    print()
    print(newStudent)

main()
