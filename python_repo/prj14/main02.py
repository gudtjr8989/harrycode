#import
import random

from pokemon.pokemon import Pokemon as create
from pokemon.cfunct import input_int
from pokemon.pokemon import Pokedex

#함수 정의
def process_atk (attacker, defender):
    print()
    print(f"{attacker.name}'s Turn")
    dmg_base=10
    dmg = round(dmg_base*(attacker.atk / defender.defense),0)
    defender.hp -= dmg
    print(f"Dealt {dmg} damage to {defender.name}! {defender.name} has {defender.hp} left! ")
    if defender.hp <= 0:
        print(f"배틀 종료! {attacker.name} 승리")
        return True
    return False

def calc_speed(x):
    x=round(10000/(x+640),0)
    return x



#Turn Calculations

#User pokemon
n=input_int("Choose your Pokemon:")
if n<=151:
    user = create(Pokedex[n-1][0],Pokedex[n-1][1],Pokedex[n-1][2],Pokedex[n-1][3],Pokedex[n-1][4],Pokedex[n-1][5],
                  Pokedex[n-1][6],Pokedex[n-1][7],Pokedex[n-1][8],Pokedex[n-1][9])
#Hidden Character
hidden = False
if n==970522:
    from pokemon.pokemon import ashistrash
    com = create(ashistrash[0], ashistrash[1], ashistrash[2], ashistrash[3], ashistrash[4], ashistrash[5],
                  ashistrash[6], ashistrash[7], ashistrash[8], ashistrash[9])
    hidden = True
    print("You have chosen a hidden character for your enemy")
    n = input_int("Choose your Pokemon:")
if n==980522:
    from pokemon.pokemon import ashistrash
    user = create(ashistrash[0],ashistrash[1],ashistrash[2],ashistrash[3],ashistrash[4],ashistrash[5],
                  ashistrash[6],ashistrash[7],ashistrash[8],ashistrash[9])
    print("You have chosen a hidden character for your pokemon")

#Comp pokemon
if hidden == False:
    r=random.randint(1,152)
    com = create(Pokedex[r-1][0],Pokedex[r-1][1],Pokedex[r-1][2],Pokedex[r-1][3],Pokedex[r-1][4],Pokedex[r-1][5],
                 Pokedex[r-1][6],Pokedex[r-1][7],Pokedex[r-1][8],Pokedex[r-1][9])

#battle

turn_clock=0
turn_sequence=[]
while turn_clock<100000:
    turn_clock+=1
    user_turn_counter=calc_speed(user.spd)
    user_turn=turn_clock % user_turn_counter
    com_turn_counter = calc_speed(com.spd)
    com_turn=turn_clock % com_turn_counter
    if user_turn == 0:
        process_atk(user, com)
        is_finish = process_atk(user, com)
        if is_finish: break
    if com_turn == 0:
        process_atk(com, user)
        is_finish = process_atk(com, user)
        if is_finish: break



