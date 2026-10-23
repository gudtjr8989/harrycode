#pokemon
class Pokemon:
    # name=input("Name of Pokemon: ")
    # hp=input(f"HP stat of {name}")
    def __init__(self,name,hp):
        self.name = name#(self)현재 객체 안에 변수를 만드는 것
        self.hp = hp

# def print_info(self):
#     print(f"Name:{self.name},hp:{self.hp}")

    def __str__(self):#앞으로 이건 무조건 추가 해주자
        return f"{self.name}/{self.hp}"

#기본 구조
#class ____:
#   def __init___:
        #변수할당
#   def __str__
        #return f"{}변수들