#Create a Student class with private attributes __name, __roll_no, and __marks. Implement 
# getter methods that return the values with validation (e.g., name should not be empty, 
# roll number between 1 and 100, marks cannot be negative). Implement setter methods that 
# allow updating the attributes only if the new values are valid, otherwise return 
# an error message. Demonstrate creating a Student object and using the getters and setters.
class Student:
    def __init__(self, name, roll_no, marks):
        print("Student constructor is called")
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks 

    # Getter methods with validation
    def get_name(self):
        if self.__name != None and self.__name != " ":
            return self.__name
        else:
            return "name not found"

    def get_roll_no(self):
        if self.__roll_no >= 1 and self.__roll_no <= 100:
            return self.__roll_no
        else:
            return "invalid roll no"

    def get_marks(self):
        if self.__marks >= 0:
            return self.__marks
        else:
            return "negative marks"

    # Setter methods with validation
    def set_name(self, new_name):
        if new_name != None and new_name != " ":
            self.__name = new_name
            return self.__name
        else:
            return "invalid name"

    def set_roll_no(self, new_roll_no):
        if new_roll_no >= 1 and new_roll_no <= 100:
            self.__roll_no = new_roll_no
            return self.__roll_no
        else:
            return "invalid roll no"

    def set_marks(self, new_marks):
        if new_marks >= 0:
            self.__marks = new_marks
            return self.__marks
        else:
            return "invalid marks"

# Example usage
stu1 = Student("Anushka", 9, 89)

# Getters
print(stu1.get_name())       # Anushka
print(stu1.get_roll_no())    # 9
print(stu1.get_marks())      # 89

# Setters
print(stu1.set_name("Himanshu"))   # Himanshu
print(stu1.set_roll_no(10))        # 10
print(stu1.set_marks(95))          # 95

# Trying invalid updates
print(stu1.set_name(" "))          # invalid name
print(stu1.set_roll_no(150))       # invalid roll no
print(stu1.set_marks(-5))          # invalid marks
