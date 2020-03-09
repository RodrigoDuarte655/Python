class Student():
    # pass
    def __init__(self, full_name, major, enrollment, first_year, current_year, semester):
        self.full_name = full_name
        # self.full_name = input('')
        self.major = major
        self.enrollment = enrollment
        self.first_year = first_year
        self.current_year = current_year
        self.semester = semester

    def info(self):
        return 'Name: {}\nMajor: {}\nEnrollment: {}\nFirst Year: {}\nCurrent Year: {}\nCurrent Semester: {}'.format(self.full_name, self.major, self.enrollment, self.first_year, self.current_year , self.semester)

    def change_date(self):
        self.current_year += 1
        self.semester += 1
            

# f_name = input('')
# maj = input('')
# enroll = int(input(''))
# f_year = int(input(''))
# l_year = int(input(''))
# semes = int(input(''))

# Rodrigo = Student(f_name, maj, enroll, f_year, l_year, semes)

Rodrigo = Student('Rodrigo Duarte Silva Luz', 'Information System', 2019003520, 2019, 2020, 3)

print(Rodrigo.info())
print()
# print(Student.info(Rodrigo))

print('{} and {}'.format(Rodrigo.current_year, Rodrigo.semester))

Rodrigo.change_date()

print('{} and {}'.format(Rodrigo.current_year, Rodrigo.semester))
