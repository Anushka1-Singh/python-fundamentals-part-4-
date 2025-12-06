class Student:
    clg_name="bhu"
    PI=3.1
    def __init__(self,name,cgpa):
        print("constructor is called")
        self.name=name
        self.cgpa=cgpa
        self.PI=3.14
    def get_cgpa(self):
        return self.cgpa
stu1=Student("anush",9.0)
print(stu1.name,stu1.cgpa)
print(stu1.get_cgpa())
print(stu1)
print(f"{stu1.name} has cgpa ={stu1.get_cgpa()}")
print(Student.clg_name)
print(stu1.clg_name)
print(stu1.PI)
print(Student.PI)