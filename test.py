# 42차시 4. 문자열 - 연습문제 7
# line=input()
# for k in range(len(line)):
#     if k%2==0:
#         print(line[k],end="")

# 44차시 5. 객체지향 - 연습문제 1
# class student:
#     def __init__(self, Korean, English, Math):
#         self.Korean=Korean
#         self.English=English
#         self.Math=Math

#     def total(self):
#         print(self.Korean+self.Math+self.English)
#         return self.Korean+self.Math+self.English


# line=input()
# k=int(line.split(', ')[0])
# e=int(line.split(', ')[1])
# m=int(line.split(', ')[2])

# stu=student(k,e,m)
# print("국어, 영어, 수학의 총점: {0}".format(stu.total()))

#45차시 5. 객체지향 - 연습문제 2

# class Korean:
#     @staticmethod
#     def printNationality():
#         print("대한민국")

# Korean.printNationality()
# Korean.printNationality()

# 46차시 5. 객체지향 - 연습문제 3

class Student:
    def __init__(self,name):
        self.name=name

    def printName(self):
        print("이름: "+self.name)

class GraduateStduent(Student):
    def __init__(self,name,major):
        self.name=name
        self.major=major
    
    def printGS(self):
        print("이름: {0}, 전공: {1}".format(self.name,self.major))


hong=Student("홍길동")
lee=GraduateStduent("이순신","컴퓨터")

hong.printName()
lee.printGS()
