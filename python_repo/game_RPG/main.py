from unittest import case

from custom_functions.cfunct import input_int

time_count=10
game_status=True

#S=[hp,atk,defs,spd]
vayne=[694,30,2,123]
teemo=[423,28,0,141]
blind_count=0
q_cd=0

def teemo_e(x):
    dmg=[10,20,30,40]
    return dmg[x]
def teemo_q(x):
    name="Blinding Darts"
    dmg=[50,85,120,155]
    blind_dur=[175,225,300,375]
    cd = 300
    q=[name,dmg[x],blind_dur[x],cd]
    return q


turn_menu=[
    [1, "Attack"],
    [2,"Skill Q"],
    [3,"Skill W"],
    [4,"Skill E"],
    [5, "Skill R"]
]

def print_menu():
    for i in range(0,len(turn_menu)):
        print(f"{turn_menu[i][0]}. {turn_menu[i][1]}")


def turn(time_count,blind_count,q_cd):
    turn_end=False
    while turn_end==False:
        print(f"Teemo Turn!: {time_count/100}")
        print_menu()
        n=input_int("Choose you move")
        match n:
            case 1:
                print(f"Teemo attacked!Dealt {teemo[1]} damage! ")
                vayne[0]=vayne[0]-teemo[1]
                turn_end=True
            case 2:

                if q_cd < time_count:
                    q=teemo_q(2)
                    print(f"Teemo used {q[0]}!!")
                    print(f"Teemo and dealt{q[1]} damage and blinded vayne for {q[2]/100} seconds")
                    vayne[0] = vayne[0] - q[1]
                    blind_count=time_count + q[2]
                    q_cd=time_count+q[3]
                    turn_end=True
                else:
                    print(f"Blinding Dart is on cooldown!")

            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
    d=[blind_count, q_cd]
    return d


while game_status==True:
    time_count=time_count+1
    vayne_turn=time_count % vayne[3]
    teemo_turn = time_count % teemo[3]

    if vayne_turn==0:
        print("Vayne Turn!")
        if blind_count>time_count:
            print("Vayne's attack missed")
        else:
            print(f"Vayne attacked!Dealt {vayne[1]} damage! ")
            teemo[0]=teemo[0]-vayne[1]
        if teemo[0]<=0:
            print("Teemo was defeated!")
            game_status=False
        else:
            print(f"Teemo has {teemo[0]} hp left")

    if teemo_turn==0:
        turn_end=False
        d=turn(time_count,blind_count,q_cd)
        blind_count = d[0]
        q_cd=d[1]

