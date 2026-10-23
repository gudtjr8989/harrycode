#0. 종료하기
#1. 등록하기
#2. 조회하기
from unittest import case
import cfunct


# 1. Setup
menu=[
    [0,"종료하기"],
    [1,"도서 등록하기"],
    [2,"도서 조회하기"]
]
book_list=[]

# 2. Define Functions
def print_menu():
    for i in range(0,len(menu)):
        print(menu[i][0],". ", menu[i][1])

def insert_book():
    print(f"=== {menu[n][1]} ===")
    print("*등록 종료시 escape을 입력해주새요")
    t=input("도서명: ")
    if t != "escape":
        p=cfunct.input_int("도서 가격:")
        d={
            "title":t,
            "price":p
        }

        book_list.append(d)
        print("도서명 등록완료")
        ex=True
    else:
        ex=False
    return ex

def select_book():
    print(f"=== {menu[n][1]} ===")
    print("Title // Price")
    for d in book_list:
        print(f"{d["title"]} // {d["price"]}")
    print("======================")
    end=input("When you are finished please press Y: ")

#프로그램
while True:
    print_menu()
    n=cfunct.input_int("메뉴를 선택해주세요: ")
    match n:
        case 0: print("종료하겠습니다");break
        case 1:
            insert_status=True
            while insert_status==True:
                insert_status=insert_book()
        case 2: select_book()

