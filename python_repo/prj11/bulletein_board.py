import cfunct


main_menu=[
    [1,"게시글 작성"],
    [2,"게시글 목록"]]
board_list=[]


def prin_main_menu():
    print(main_menu)

def insert_board():
    print("=== 게시글 작성 ====")
    t=input("title: ")
    c=input("content: ")
    d={
        "title":t,
        "content":c
    }
    board_list.append(d) #리스트에 추가하는 작업
    print("게시글 작성완료")


def select_board():
    print("=== 게시글 목록 ===")
    for d in board_list:
        print(d["title"]," // ", d["content"])

while True:
    print("====== BOARD ======")
    for d in main_menu:
        print(d)

    n=cfunct.input_int("메뉴를 선택해주세요")
    match n:
        case 1:
            print("=== 게시글 작성")
            insert_board()
        case 2:
            select_board()


