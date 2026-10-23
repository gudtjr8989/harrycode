# 90
# ~ 100: A
# 70
# ~   89: B
# 40
# ~   69: C
# 0
# ~   39: D

score=int(input(""))
score_crit=(100,89,69,39,-1)
score_class=("A","B","C","D")
dummy=False
count=0
while dummy==False:
    if score>score_crit[count+1]:
        print(f"{score_class[count]}")
        dummy=True
    else:
        count=count+1