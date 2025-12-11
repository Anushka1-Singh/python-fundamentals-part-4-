#POLYMORPHISM
# function overiding
class Employee:
    def get_designation(self):
        print("designation = employee")

class Teacher(Employee):
    def get_designation(self):
        print("designation = teacher")
t1 = Teacher()
t1.get_designation()
t2 = Employee()
t2.get_designation()
