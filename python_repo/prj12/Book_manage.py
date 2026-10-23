#도서관리 시스템
import cfunct

class Book:
    def __init__(self,a,b):
        self.title = a
        self.price = b

book_list=[]

menu=[
    [0,"종료"],
    [1,"도서 등록"],
    [2,"도서 조회"]
]
def print_menu():
    for i in range(0,len(menu)):
        print(f" {menu[i][0]}. {menu[i][1]}")

def insert_book():
    print(f"=== {menu[1][1]} ===")
    bookname=input("도서명 :")
    price=cfunct.input_int("도서 가격")
    x=Book(bookname,price)
    book_list.append(x)
    print("도서 등록 완료!")

def select_book():
    print(f"=== {menu[2][1]} ===")
    for x in book_list:
        print(f" {x.title}//{x.price}")


while True:
    print_menu()
    n=cfunct.input_int("메뉴 번호를 선택해주세요: ")
    # n = int(input("메뉴 번호를 선택해주세요: "))
    match n:
        case 0:
            break
        case 1:
            insert_book()
        case 2:
            select_book()
        case _:
            pass
