a_speed=80
b_speed=61
def calc_speed(x):
    x=round(10000/(x+64),0)
    return x

a= calc_speed(a_speed)
b= calc_speed(b_speed)
print(a)
print(b)
turn_clock=0
turn_sequence=[]
while turn_clock<10000:
    turn_clock=turn_clock+1
    if turn_clock%a==0:
        turn_sequence.append(["A",turn_clock])
    if turn_clock%b==0:
        turn_sequence.append(["B",turn_clock])
    else:
        pass
print(turn_sequence)

