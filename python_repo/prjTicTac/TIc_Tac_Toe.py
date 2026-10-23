import random

#1. Introduction####
print("==Welcome to Tic Tac Toe==")
# print(" Can you defeat us in simple game?")
user_name1=input("Tell me your name Player 1:")
user_name2=input("Tell me your name Player 2:")
print(f"Welcome {user_name1}, {user_name2}!")

#2. Who goes first?
game_status=True #True 일시 Game 진행, False 일시 Game 종료
player_turn=input(f"Would {user_name1} like to move first or second? For first type Y for second type N: ")
while player_turn!=True and player_turn!=False :
    if player_turn=="Y" or player_turn=="y":
        player_turn=True
    elif player_turn=="N" or player_turn=="n":
        player_turn=False
    else:
        player_turn=input("Error!! Please enter Y or N: ")
# player_turn=True #True 일때 사용자턴, False 일떄 Game 종료


comp_board=[0,1,2,3,4,5,6,7,8]
tracker=([0,0,0,0,0,0,0,0,0])
displayed_status=(["  ","  ","  ","  ","  ","  ","  ","  ","  "])
count_turns=0
player_choice_x=0
player_choice_y=0
xchoice_dummy=False
input_dummy=False #True일시 값을 받아들임

while game_status==True and count_turns<9:
    #사용자 턴 행동
    if player_turn==True and game_status==True:
        print(f"{user_name1} Turn!")
        print("R3|",f" {displayed_status[6]} ","|",f" {displayed_status[7]} ","|",f" {displayed_status[8]} ","|")
        print("R2|",f" {displayed_status[3]} ","|",f" {displayed_status[4]} ","|",f" {displayed_status[5]} ","|")
        print("R1|",f" {displayed_status[0]} ","|",f" {displayed_status[1]} ","|",f" {displayed_status[2]} ","|")
        print("   "," C1 "," "," C2 "," "," C3 "," ")
        input_dummy=False
        while input_dummy == False: #검증후 x값을 받아들임
            player_choice_x = input("Please write down the x-coordinates u want to place :")
            if player_choice_x in ["1", "2","3"]:
                player_choice_x = int(player_choice_x)-1
                input_dummy=True
            else:
                print("Error Please Try again down below")
        input_dummy=False
        while input_dummy == False: #검증후 y값을 받아들임
            player_choice_y = input("Please write down the x-coordinates u want to place :")
            if player_choice_y in ["1", "2","3"]:
                player_choice_y = int(player_choice_y)-1
                input_dummy=True
            else:
                print("Error Please Try again down below")
        coord_to_num=player_choice_x+3*player_choice_y
        if tracker[coord_to_num]==0: #중복확인 작업
            tracker[coord_to_num]=1
            displayed_status[coord_to_num]="P1"
            player_turn = False
            count_turns = count_turns + 1
        else:
            print("ERROR:That place has been already taken!")

#승리조건 확인창
    #ROW 확인
    for i in range(0, 3):  # i for row
        sum_value = 0
        for j in range(0, 3):  # j for column
            sum_value = sum_value + tracker[3 * i + j]
        check_value = sum_value * sum_value
        if check_value == 9:
            game_status = False
            print(f"Row {i + 1} Tic_Tac_Toe Game has Ended!")
            break
    #Column 확인
    for j in range(0, 3):  # j for column
        sum_value = 0
        for i in range(0, 3):  # i for row
            sum_value = sum_value + tracker[3 * i + j]
        check_value = sum_value * sum_value
        if check_value == 9:
            game_status = False
            print(f"Column {i + 1} Tic_Tac_Toe Game has Ended!")
            break
    for i in range(0,3):
        sum_value = 0
        sum_value = sum_value + tracker[4*i]
    check_value = sum_value * sum_value
    if check_value == 9:
        game_status = False
        print(f"Diagonal Win! Tic_Tac_Toe Game has Ended!")
        break
    for i in range(0,3):
        sum_value = 0
        sum_value = sum_value + tracker[2*i*+2]
    check_value = sum_value * sum_value
    if check_value == 9:
        game_status = False
        print(f"Diagonal Win! Tic_Tac_Toe Game has Ended!")
        break

    if count_turns == 9:
        game_status == False
        break


    # 컴퓨터 턴 행동
    elif player_turn==False and game_status==True:
        print(f"{user_name2} Turn!")
        print("R3|", f" {displayed_status[6]} ", "|", f" {displayed_status[7]} ", "|", f" {displayed_status[8]} ", "|")
        print("R2|", f" {displayed_status[3]} ", "|", f" {displayed_status[4]} ", "|", f" {displayed_status[5]} ", "|")
        print("R1|", f" {displayed_status[0]} ", "|", f" {displayed_status[1]} ", "|", f" {displayed_status[2]} ", "|")
        print("   ", " C1 ", " ", " C2 ", " ", " C3 ", " ")
        input_dummy = False
        while input_dummy == False:  # 검증후 x값을 받아들임
            player_choice_x = input("Please write down the x-coordinates u want to place :")
            if player_choice_x in ["1", "2", "3"]:
                player_choice_x = int(player_choice_x) - 1
                input_dummy = True
            else:
                print("Error Please Try again down below")
        input_dummy = False
        while input_dummy == False:  # 검증후 y값을 받아들임
            player_choice_y = input("Please write down the x-coordinates u want to place :")
            if player_choice_y in ["1", "2", "3"]:
                player_choice_y = int(player_choice_y) - 1
                input_dummy = True
            else:
                print("Error Please Try again down below")
        coord_to_num = player_choice_x + 3 * player_choice_y
        if tracker[coord_to_num]==0:
            tracker[coord_to_num]=-1
            displayed_status[coord_to_num]="P2"
            player_turn=True
            count_turns=count_turns+1
        else:print("ERROR:That place has been already taken!")

#승리조건 확인창
    #ROW 확인
    for i in range(0, 3):  # i for row
        sum_value = 0
        for j in range(0, 3):  # j for column
            sum_value = sum_value + tracker[3 * i + j]
        check_value = sum_value * sum_value
        if check_value == 9:
            game_status = False
            print(f"Row {i + 1} Tic_Tac_Toe Game has Ended!")
            break
    #Column 확인
    for j in range(0, 3):  # j for column
        sum_value = 0
        for i in range(0, 3):  # i for row
            sum_value = sum_value + tracker[3 * i + j]
        check_value = sum_value * sum_value
        if check_value == 9:
            game_status = False
            print(f"Column {j + 1} Tic_Tac_Toe Game has Ended!")
            break
    #y=x선 확인
    for i in range(0,3):
        sum_value = 0
        sum_value = sum_value + tracker[4*i]
    check_value = sum_value * sum_value
    if check_value == 9:
        game_status = False
        print(f"Diagonal Win! Tic_Tac_Toe Game has Ended!")
        break
    #y=-x선확인
    for i in range(0,3):
        sum_value = 0
        sum_value = sum_value + tracker[2*i*+2]
    check_value = sum_value * sum_value
    if check_value == 9:
        game_status = False
        print(f"Diagonal Win! Tic_Tac_Toe Game has Ended!")
        break

if count_turns==9:
    print("It is a Tie!")

#Final Board
print("R3|",f" {displayed_status[6]} ","|",f" {displayed_status[7]} ","|",f" {displayed_status[8]} ","|")
print("R2|",f" {displayed_status[3]} ","|",f" {displayed_status[4]} ","|",f" {displayed_status[5]} ","|")
print("R1|",f" {displayed_status[0]} ","|",f" {displayed_status[1]} ","|",f" {displayed_status[2]} ","|")
print("   "," C1 "," "," C2 "," "," C3 "," ")

#인곻지능 개발
# 시계 방향 90 변환후 - 대각축 대칭으로 모든 면 인식가능
# 촤선 시나리오 작성
# (4,0,2,6,3)-무승부
# (4,1*,6,2,0)- 무조건승
# (0,5*,4,8,2) - 무조건승
# (0,1*,4,8,2) - 무조건승
# (0,2,8,4,6) - 무조건 승
# (0,4)-무승부
# (0,8*)- 무조건승
# (1,0 - 무승부
# (1,4 - 무승부
# (1,5* - 무조건 승
# (1,7 - 무승부
# (1,8* -무조건 승
