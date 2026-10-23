# 캐리터 정보 수정
#0. Import functions
from custom_functions.cfunct import input_int

#1. Background 정의
"1.1 menu정의"
menu=[
    (0,"종료하기"),
    (1,"캐릭터 추가"),
    (2,"캐릭터 수정"),
    (3,"캐릭터 조회"),
    (4,"캐릭터 상세 설명"),
    (5,"캐릭터 삭제")
]
"1.2 baste_stat정의"
base_stat=[
    {"hp":"b_hp"},
    {"atk":"b_atk"},
    {"def":"b_def"},
    {"spd":"b_spd"},
    ]
"1.3 Character List"
character_list=[]
""



#2. 함수 정의

##2.0 Menu 프린트
def print_menu(): #메뉴판 호출
    for i in range(0,len(menu)):
        print(f"{menu[i][0]}. {menu[i][1]}")
##1.1캐릭터 추가
###1.1.1 캐릭터 추가 class
class character: #캐릭터 정보
    def __init__(self, name, stat):
        self.name = name
        self.stat = stat
###1.1.2 캐릭터추가 함수
def add_char():
    print("=== 캐릭터 추가 ====")
    name=input("Name of Character: ")
    stat=input_int("Character Stat: ")
    x=character(name,stat)
    character_list.append(x)
    print("Successfully added new character")
## 3.캐릭터 조회
###
def view_char():
    print("Character Name     //    Stat")
    for i in range (0,len(character_list)):
        print(f"{character_list[i].name}//{character_list[i].stat}")

# . 프로그램
while True:
    print_menu()
    n=input_int("Please select the menu: ")

    match n:
        case 0:
            break
        case 1:
            add_char()
    #     case 2:
    #         edit_char()
        case 3:
            view_char()
    #     case 4:
    #         view_detail()
    #     case 5:
    #         delete_char()





