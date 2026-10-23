#1.등록
#2.조회

main_menu=[[1,"도서 등록"],
           [2,"도서 조회"],
           [3,"도서 상세 조회"],
           [4,"도서 수정 하기"],
           [5,"도서 삭제하기"],
           [0,"프로 그램종료"]]

book_list=[] #도서 총 목록

def input_price():
    status=True
    test=True
    while status==True:
        x = input("도서 가격: ")
        for i in range(len(x)): #검사
            if x[i] in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                pass
            else:
                test = False
                break
        if test==False:
            "Error! Please Retry"
            continue
        else:
            x=int(x)








    return x

def insert_book():
    while True:
        t = input("도서 제목: ")
        if t == ("exit"):
            break
        p=input_price()
        d={"title":t,
           "price":p
        }
        book_list.append(d)
        print(f"도서 등록 완료!: {t} / {p}")



def select_book():
    print("  제목  /  가격  ")
    for d in book_list:
        print(f"{d['title']} / {d['price']}")


def select_one_book():
    pass

def update_book():
    pass

def delete_book():
    pass



def print_main_menu():
    print("======= 도서 관리 프로그램 =======")
    for i in range (0,len(main_menu)):
        print(f"{main_menu[i][0]}. {main_menu[i][1]}")

while True:
    print_main_menu()
    n = input("어떤 것을 진행 하겠습니까?")
    if n in ["1","2","3","4","5","6","7","8","9","0"]:
        n=int(n)
    else:
        print("Error Please Retry:")
        continue


    match n:
        case 1: #도서 등록
            print(f"=== {main_menu[n-1][1]} ===")
            insert_book()

        case 2: #도서 조회
            print(f"=== {main_menu[n-1][1]} ===")
            select_book()
            wait=input("Press Enter to continue...")

        case 3: #도서 상세 조회
            print(f"=== {main_menu[n-1][1]} ===")
            select_one_book()

        case 4: # 도서 수정하기
            print(f"=== {main_menu[n-1][1]} ===")
            update_book()

        case 5: #도서 삭제하기
            print(f"=== {main_menu[n-1][1]} ===")
            delete_book()

        case 0:
            print("시스템 종료")
            break

        case _: #오류
            print("올바른 메뉴를 입력하세요")


print(book_list)
