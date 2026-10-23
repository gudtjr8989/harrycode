#영어 단어 : 뜻
import random
words={
    "apple":"사과",
    "banna":"바나나",
    "orange":"오렌지"
}

#강사님 풀이
#w
count=0
right=0
for k,v in words.items(): #이런식으로 튜플을 받아줄수있음 튜플 분해할당 할수 있음
    x=input(f"Guess the {k}: ")
    if x==v:
        print("정답입니다")
        count+=1
        right+=1
    else:
        print("Wrong")
        count+=1
print(f"정답률:{right/count*100}%")
# print(words.get("apple"))
