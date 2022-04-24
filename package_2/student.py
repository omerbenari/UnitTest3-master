class student:
    def __init__(self, id:int, age:int, name:str):
        if type(id) != int:
            raise TypeError ("id must be a number")
        if type(name) != str:
            raise TypeError ("name must be a string")
        if type(age) != int:
            raise TypeError ("age must be a number")
        if age<0 or age>120:
            self.age=0
        else:
            self.age=age
        self.id = id
        self.age = age
        self.name = name
        self.grades={}


    def add_grades(self, subject, grade:int):
        if type(subject) != str:
            raise TypeError("subject must be a string")
        if type(grade) != int:
            raise TypeError("grade must be a number")

        self.grades[subject]=grade


    def __repr__(self):
        return f"{self.id}, {self.name}, {self.age}, {self.grades}"


    def calc_factor(self, subject, percentage:int):
        if type(subject) != str:
            raise TypeError("subject must be a string")
        if type(percentage) != int:
            raise TypeError("percetage must be a number")

        self.grades[subject]+=(percentage/100)*self.grades[subject]
        if self.grades[subject] > 100:
            self.grades[subject] = 100


    def average(self):
        # dont divide by zero
        if len(self.grades) != 0:
            avg = sum(self.grades.values())/len(self.grades)
            return avg
        else:
            print("this student doesnt have any grades")
            return False


    def __eq__(self, other):
        if type(other) != student:
            return False
        if self.id == other.id:
            return True
        else:
            return False


    def __gt__(self, other):
        if type(other) != student:
            raise TypeError("you cannot compare these items because they are not the same type")
        if self.age > other.age:
            return True
        else:
            return False

#if __name__ == "__main__":
    #student_invalid_id = student("asd", "sdf", 21)