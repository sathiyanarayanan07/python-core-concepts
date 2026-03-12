class Student:
    def __init__(self,name,student_id):
        self.name =name
        self.student_id =student_id
        self.__grades = []

    def add_grades(self,grade):
        if 0 <= grade <= 100:
            self.__grades.append(grade)   
        else:
            print("Invaild grade. Must be between 0 and 100.")

    def get_average(self):
        if not self.__grades:
            return 0
        return sum(self.__grades) / len(self.__grades)
    

class GraduateStudent(Student):
    def __init__(self, name, student_id, thesis_topic):
        super().__init__(name, student_id)
        self.thesis_topic = thesis_topic


class School:
    def __init__(self):
        self.students = []

    def enroll(self , student_object):
        self.students.append(student_object)

    def show_report_card(self):
        for student in self.students:
            print("Name:", student.name)
            print("student_id:", student.student_id)
            print("Average Grade:", student.get_average())

s1 = Student("Alice", 1)            
s1.add_grades(80)
s1.add_grades(90)


school= School()

school.enroll(s1)

school.show_report_card()