class Student:
    def __eq__(self, other):
        return self.avg() == other.avg()
    def __ne__(self, other):
        return self.avg() != other.avg()
    def __lt__(self, other):
        return self.avg() < other.avg()
    def __add__(self, other):
        return self.avg() + other.avg()
    def __mul__(self, other):
        return self.avg() * other.avg()
    def __neg__(self, other):
        return self.avg() - other.avg()

    def avg(self):
        avg = 0
        summ = 0
        length = 0
        for i in self.courses_in_progress:
            if i in self.grades:
                summ += sum(self.grades[i])
                length += len(self.grades[i])
        avg = summ/length
        return avg

    def __str__(self):
        s = ','
        print(f'Имя: {self.name}')
        print(f'Фамилия: {self.surname}')
        print(f'Средняя оценка за домашние задания: {self.avg()}')
        print(f'Курсы в процессе изучения: {s.join(self.courses_in_progress)}')
        return(f'Завершенные курсы: {s.join(self.finished_courses)}')

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def GiveAssessment(self, mentor, grade, course_name):
        if isinstance(mentor, Lecturer) and course_name in mentor.courses_attached and course_name in self.courses_in_progress:
            if course_name in mentor.dictin:
                mentor.dictin[course_name] += [grade]
            else:
                mentor.dictin[course_name] = [grade]
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Reviewer(Mentor):
    def __str__(self):
        print(f'Имя: {self.name}')
        return(f'Фамилия: {self.surname}')

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __eq__(self, other):
        return self.avg() == other.avg()
    def __ne__(self, other):
        return self.avg() != other.avg()
    def __lt__(self, other):
        return self.avg() < other.avg()
    def __add__(self, other):
        return self.avg() + other.avg()
    def __mul__(self, other):
        return self.avg() * other.avg()
    def __neg__(self, other):
        return self.avg() - other.avg()

    def avg(self):
        avg = 0
        summ = 0
        length = 0
        for i in self.courses_attached:
            if i in self.dictin:
                summ += sum(self.dictin[i])
                length += len(self.dictin[i])
        avg = summ/length
        return(avg)

    def __str__(self):
        print(f'Имя: {self.name}')
        print(f'Фамилия: {self.surname}')
        return(f'Средняя оценка за лекции: {self.avg()}')

    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.dictin = {}



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_lecturer = Lecturer('Denis', 'Vaulin')
cool_lecturer.courses_attached += ['Python']

cool_lecturer1 = Lecturer('Saveliy', 'Boychyk')
cool_lecturer1.courses_attached += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

best_student.GiveAssessment(cool_lecturer1, 9, 'Python')
best_student.GiveAssessment(cool_lecturer, 10, 'Python')

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student)