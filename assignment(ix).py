#ABSTRACTION
#Abstraction hides complex implementation details and shows only essential features
#  using an abstract base class. Abstract classes cannot be instantiated and act
#  as a blueprint for subclasses, which must implement the abstract methods to create objects.

from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self, base_salary, factor1, factor2):
        pass
class Intern(Employee):
    def calculate_salary(self, base_salary, factor1, factor2):
        # factor1 = work_hours, factor2 = 1 (unused)
        return f"Intern salary {base_salary * factor1}"
class FullTimeEmployee(Employee):
    def calculate_salary(self, base_salary, factor1, factor2):
        # factor1 = experience, factor2 = work_hours
        return f"Full time salary {base_salary * factor1 * factor2}"
class ContractEmployee(Employee):
    def calculate_salary(self, base_salary, factor1, factor2):
        # factor1 = period, factor2 = months
        return f"Contract salary {base_salary * factor1 * factor2}"
i1=Intern()
print(i1.calculate_salary(500,5,1))
i2=FullTimeEmployee()
print(i2.calculate_salary(1000,5,6))
i3=ContractEmployee()
print(i3.calculate_salary(700,5,8))

#This program demonstrates abstraction using an abstract base class Employee.
#The abstract method calculate_salary defines a common interface, and each subclass implements 
#its own salary calculation logic. Objects are created from subclasses, not the abstract class.
