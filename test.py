# 47차시 5. 객체지향 - 연습문제 4
# class Circle:
#     PI=3.14
#     def __init__(self, half):
#         self.half=half
    
#     def space(self):
#         return pow(self.half,2)*self.PI

# cir=Circle(2)
# print("원의 면적: %0.2f"%cir.space())

# 48차시 5. 객체지향 - 연습문제 5

# class Rectangle:
#     def __init__(self, width, height):
#         self.width=width
#         self.height=height

#     def square(self):
#         return self.width*self.height

# r=Rectangle(4, 5)
# print("사각형의 면적: %d"%r.square())

# 49차시 5. 객체지향 - 연습문제 6

# class Shape:
#     def area():
#         return 0

# class Square(Shape):
#     def __init__(self, length):
#         self.length=length
#     def area(self):
#         return pow(self.length,2)

# s=Square(3)
# print("정사각형의 면적: {0}".format(s.area()))

# 50차시 5. 객체지향 - 연습문제 7

class Person:
    def getGender():
        return "Unknown"

class Male(Person):
    def getGender(self):
        return "Male"

class Female(Person):
    def getGender(self):
        return "Female"

m=Male()
f=Female()
print(m.getGender())
print(f.getGender())