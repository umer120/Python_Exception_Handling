class InvalidGradeException(Exception):
    def __init__(self,grade,message="Grade is not between 0 and 100"):
        self.grade=grade
        super().__init__(f"{message} since grade:{grade}")


class Student:
    name=""
    grade=0.0
    def __init__(self,name,grade):
        if 0<=grade<=100:
            self.name=name
            self.grade=grade
            print("Attributes assigned successfully!")
        else:
            raise InvalidGradeException(grade)


try:
    s1=Student("Umer",95) # Valid for 1st student since grade is between 0 and 100
    s2=Student("Haider",-2) # Invalid since grade is less than 0
except InvalidGradeException as g:
    print(f"Grade issue: {g}")

