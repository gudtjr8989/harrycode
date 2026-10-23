from pokemon import Pokemon
from animal import Animal
from study.practice.athelete import Athelete
from study.practice.food import Food
from study.practice.hero_stat import stat

# animal_list=[]
# print("객체 만들기")
# # n=input("동물명: ")
# # w=input("몸무게: ")
# # t=input("종류: ")
# x=Animal("Harry",54,"Human")
# print(x.name,x.weight,x.type)
# print(type(x))
# y=Animal("Penguin",1000,"Legendary")
# print(y.name,y.weight,y.type)
# print(type(y))
# z=Animal("Tiger",1000,"Cat")
# print(z.name,z.weight,z.type)
# print(type(z))
#
# p1=Pokemon("Pikachu",100)
# p2=Pokemon("Raichu",100)
# p3=Pokemon("Charmander",100)

# print(p1)#그냥 객체를 쓰면 무조건 파이썬은 기본적으로 __str__이걸 output 해줌
# print(p2)
# # print(p3)
# f1=Food(name="Ramen",type="instant",price=10000,place="japanese",descr="신라면",calories=20000,style=2222)
# print(f1)
#
#
# h1=stat("Tassadar",10000,200,50,10,150)
# print(h1)
# print(h1.__list__())

a1=Athelete("박지성",53,194,95)
print(a1)
a1.eat()