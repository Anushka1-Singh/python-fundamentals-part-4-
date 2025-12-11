class Shape:
    def area(self, value1, value2):
        return value1*value2
class Circle(Shape):
    def area(self, pi ,radius):
        return pi*radius*radius
class Rectangle(Shape):
    def area(self, length, breadth):
        return length*breadth
class Triangle(Shape):
    def area(self, base, height):
        return 1/2*base*height
s1=Circle()
print(s1.area(5))
s2=Rectangle()
s3=Triangle()
print(s2.area(6,9))
print(s3.area(9,8))
      
              
