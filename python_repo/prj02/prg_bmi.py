username=input("혹시 성함이 어떻게 되십니까\n")
age=int(input("나이는 어떻게 되세요? (cm)\n"))
height=int(input("키는 어떻게되세요?(cm)\n"))
weight=int(input("몸무게는 어떻게 되세요? (kg)\n"))
print("답변해주셔서 감사합니다!")

#BMI
BMI=weight/(height/100)/(height/100)
bmigoal=0

if BMI < 18.5:
    bmigoal=18.6
    weightgoal=round(bmigoal*height*height/10000,1)
    print(f"저체중 범위이십니다. 몸무게를 {weightgoal}kg 까지 늘려봐요")
elif BMI < 22.9:
    bmigoal = 22.9
    weightgoal=round(bmigoal*height*height/10000,1)
    print("정상 체중 범위입니다. 이대로 유지하세요")
elif BMI < 24.9:
    bmigoal = 22.9
    weightgoal=round(bmigoal*height*height/10000,1)
    print(f"축하합니다 {username}님!\U0001F973 당신은 막 돼지와 인간의 경계선에 있습니다! 몸무게를 {weightgoal}kg 까지 줄여서 다시 경계선을 탈출해주세요")
elif BMI < 29.9:
    bmigoal=24.9
    weightgoal=round(bmigoal*height*height/10000,1)
    print(f"{username}님은 이제 공식적으로 정말 인간이길 포기하셨군요\U0001F609! {weightgoal}kg 까지 줄여서 다시 희망을 찾아봐요")
elif BMI < 34.9:
    bmigoal=29.9
    weightgoal=round(bmigoal*height*height/10000,1)
    print(f"{username}! {age}의 나이로 심장병으로 사망하시겠네요 축하드려요!\U0001F973 미리 119에 전화를 드려둘까요? 돼지로서도 살고 싶다면 {weightgoal}kg 까지 줄여보세요")
else:
    print(f" WOW! 놀랍군요 전 {username}처럼 살찐 돼지를 본적이없습니다!")

