#import
import random
from pokemon.pokemon import Pokemon as create
from pokemon.cfunct import input_int

#함수 정의
def process_atk (attacker, defender):
    print(f"{attacker.name}의 공격")
    dmg = attacker.atk - defender.defense
    defender.hp -= dmg
    print(f"Dealt {dmg} damage to {defender.name}! {defender.name} has {defender.hp} left! ")
    if defender.hp <= 0:
        print(f"배틀 종료! {attacker.name} 승리")
        return True




n=input_int("Choose your Pokemon:")

p1=create(1, "Bulbasaur", "Grass Poison", 45, 49, 49, 65, 65, 45, 318)
p2=create(4, "Charmander", "Fire", 39, 52, 43, 60, 50, 65, 309)
p3=create(7, "Squirtle", "Water", 44, 48, 65, 50, 64, 43, 314)

match n:
    case 1: user=p1
    case 2: user=p2
    case 3: user=p3
    case _: user=None#None 아무것도 안가리킨다

# r=random.randint(1,152)
r=1
match r:
    case 1: com=p1
    case 2: com=p2
    case 3: com=p3


# print(f"{user}")
# print(f"{com}")
# print(user==com) #각각 값을비교
# print(user is com) #주소를 비교




#battle
# com--> user
# user --> com
turn_counter=0
while turn_counter < 100000:
    is_finish = process_atk(user, com)
    if is_finish: break
    process_atk(com, user)
    is_finish = process_atk(com, user)
    if is_finish: break




