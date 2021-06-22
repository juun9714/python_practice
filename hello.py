class FourCal:

    def __init__(self, first, second):
        self.first=first
        self.second=second

    def setData(self, first, second):
        self.first=first
        self.second=second

    def add(self):
        return self.first+self.second

    def minus(self):
        return self.first-self.second

    def mul(self):
        return self.first*self.second

    def div(self):
        return self.first/self.second

class moreFourCal(FourCal):
    def pow(self):
        return self.first**self.second

class safeFourCal(FourCal):
    #FourCal에 있는 div메서드와 동일한 이름의 메서드를 선언 = Method Overriding
    #부모 클래스의 동일 이름 메서드 대신, 오버라이딩한 메서드가 실행된다.

    lastname='kwon'
    def div(self):
        if self.second==0:
            return 0
        else:
            return self.first/self.second

    def pow(self):
        if self.second==0:
            return 1
        else:
            return self.first**self.second
