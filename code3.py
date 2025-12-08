# MULTIPLE INHERITANCE - KEY POINTS:
# 1. super().__init__(parent_param) → Calls FIRST parent's __init__ with AUTO self
# 2. ParentClass.__init__(self, param) → Calls specific parent with EXPLICIT self
# 3. super() = implicit self (Python handles it automatically)
# 4. Direct class call = explicit self (you must write it)
# 5. Both methods initialize parent constructors & create memory for their attributes
# 6. TA object gets: salary(from Teacher) + gpa(from Student) + name(from TA itself)
# super() auto-passes self | Direct class call needs explicit self
# Both initialize parent constructors & create memory for their attributes

class Teacher:
    def __init__(self,salary):
        self.salary = salary
class Student:
    def __init__(self,gpa):
        self.gpa=gpa
class TA(Teacher, Student):
    def __init__(self, salary, gpa, name):
        super().__init__(salary)
        Student.__init__(self, gpa)
        self.name=name
ta1= TA(15_000, 9.3, "Shradha")
print(ta1.name, ta1.gpa, ta1.salary)


# MULTI LEVEL INHERITANCE
#so basically super in child class invokes the constructor of parent class and that will inherit the methods and attributes of parent classs truly
#Without super(), the parent's __init__ is skipped, so the parent's attributes don't get initialized properly. With super(), everything works perfectly! ✅
#class Employee:
#    start_time = "10am"
#    end_time = "5pm"
#class AdminStaff(Employee):
#    def __init__(self,role):
 #       self.role=role
#class Accountant(AdminStaff):
#    def __init__(self, salary, role):
#        super().__init__(role)
#        self.salary =salary
#acc1 = Accountant(50_000,'CA')
#print(acc1.role,acc1.salary,acc1.start_time,acc1.end_time)

# SINGLE LEVEL INHERITANCE
#class Employee:
#    start_time = "10am"
#    end_time= "5pm"
#    def change_time(self, new_end_time):
#        self.end_time=new_end_time
#class Teacher(Employee):
#    def __init__(self,subject):
#        self.subject =subject
#t1=Teacher("maths")
#t1.change_time("4pm")
#print(t1.subject,t1.start_time,t1.end_time)
        
# BASICS OF INHERITANCE
#class Employee:
#    start_time = "10am"
#
#     end_time= "5pm"
#class Teacher(Employee):
#    def __init__(self,subject):
#        self.subject =subject
#t1=Teacher("maths")
#print(t1.subject,t1.start_time,t1.end_time)

        