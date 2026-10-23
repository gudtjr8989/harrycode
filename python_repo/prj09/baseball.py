#자리일치 strike
#자리일치 하지 않고 숫자는 Ball
#아무것도 일치하지 않으면 Out

import random
r_answer=random.sample(range(1,10),3) #중복없이 뽑아내줌

answer=""
for i in range(0,3):
    answer+=str(r_answer[i])
print(answer)
print(type(answer))
# print(pred_number[0])#string에도 적용됨
# print(pred_number[1])
# print(pred_number[2])

#Strike

while True:
    pred_number = input("Guess a three digit number: ")
    strike_count = 0
    ball_count = 0
    x = 0
    for x in range (0,3):
        if pred_number[x]==answer[x]:
            strike_count+=1
        elif pred_number[x] in answer:
            ball_count+=1

    if strike_count==3:
        print(f"You win the answer was {answer}")
        break
    elif ball_count==0:
        print("Out")
    else:
        print(f"S:{strike_count}\nB:{ball_count}")

#
#
# a = pred_number[0] in answer
# b = pred_number[1] in answer
# c = pred_number[2] in answer
#
# print(a,b,c)
#
#
# # count=0
# # guess=(x.split(int()))
# # print(guess)
# # # for i in range(0,3):
# # #     guess[i]=
