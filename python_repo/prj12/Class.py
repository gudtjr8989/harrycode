#Class = 객체를 만들기 위함
#객체란= Data랑 함수 (also called as member) f.
#변수 = Snake Case
#Class = PascalCase

class Book():
    def __init__(self):
        self.a=10
        self.b=20

    def f01(self):
        print("f01 호출됨")
    def f02(self):
        print("f03 호출됨")
    def f03(self):
        print("f03 호출됨")

a=30
b=15

book=Book()#이렇게 하는게 더 좋다
book.f01()
book.f02()
book.f03()
#아래와 같이 하면 각각 매번 개체를 만듬
Book().f01()
Book().f02()
Book().f03()


class SymConv:
    def f01(self):
        pass
