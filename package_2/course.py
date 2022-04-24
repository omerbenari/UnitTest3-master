from student import student

class course:
    def __init__(self, num : int, name : str, max_students : int = 10 ):
        if type(num) != int:
            raise TypeError("course num argument must be int")
        if type(name) != str:
            raise TypeError("course name argument must be str")
        if type (max_students) != int:
            raise TypeError("max student argument must be int")
        if max_students > 10:
            max_students = 10

        self.num = num
        self.name = name
        self.subjects = {}
        self.student = []
        self.max_students = max_students

    def __repr__(self):
        return f" course number {self.num} \n" \
               f" course name {self.name} \n" \
               f"{self.subjects} \n" \
               f"{self.student} , max students : {self.max_students}"


    def add_student(self, student : student):
        if type(student) != student:
            raise TypeError("your argument must be type student")

        if len(self.student) < len(self.max_students):
            self.student.append(student)
            return True
        else:
            return False


    def add_factor(self, subject, factor):
        if type(subject) != str:
            raise TypeError("subject must be a string")
        if type(factor) != int:
            raise TypeError("factor must be a number")
        if subject not in self.subjects:
            raise ValueError("the subject isnt on this course")

        for i in self.student:
            if subject in i.grades:
                i.calc_factor(subject, factor)
            else:
                pass


    def del_student(self, student : student):
        if student in self.student:
            self.student.remove(student)
        else:
            print("student is not in this course")



