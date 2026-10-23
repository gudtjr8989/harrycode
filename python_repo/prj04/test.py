#Simulation for amount of steps required to reach destination

import random

#개시 시점 정의 변수
n=int(input("Input a number the maxmum range of a number:"))
simulation_num_req=int(input("Input the number of simulations:"))
simulation_num=0
total_calc_num1=0
total_calc_num2=0
score_method1 = 0
score_method2 = 0


while simulation_num<=simulation_num_req:
    # simulation당 재정의 변수
    x = random.randint(1, n)
    print(f"x was defined to be {x}")
    calc_num1 = 0
    calc_num2 = 0
    status = 0
    status2 = 0
    range_min = 1
    range_max = n
    guess_num = (range_min + range_max) // 2
    guess_num2 = 1

    while status==0 :
        if x>=guess_num:
            calc_num1=calc_num1+1
            if range_min==guess_num:
                status=1
                # print(f"Method 1: With {calc_num1} trials we have isolated the answer")

            else :
                # print(f"Method 1:Trial {calc_num1} failed to isolate: Range was {range_min}~ {range_max}:{guess_num} was High or even")
                range_min = guess_num
                guess_num= (range_min + range_max) // 2

        else:
            calc_num1 = calc_num1 + 1
            if range_min == guess_num:
                status = 1
                # print(f"Method 1:With {calc_num1} trials we have isolated the answer")

            else:
                # print(f"Method 1:Trial {calc_num1} failed to isolate: Range was {range_min}~ {range_max}:{guess_num} was Low")
                range_max = guess_num
                guess_num = (range_min + range_max) // 2

    while status2==0:
        if guess_num2==x:
            calc_num2 = calc_num2 + 1
            status2=1
            # print(f"Method 2: With {calc_num2} trials we have isolated the answer")
        else:
            calc_num2 = calc_num2 + 1
            # print(f"Method2: We guessed the answer {guess_num2} and was wrong we are at trial {calc_num2}")
            guess_num2=guess_num2+1

    if calc_num1<calc_num2:
        # print(f"For x={x} Method 1 isolated the answer faster then method 2. {calc_num1} VS {calc_num2},{calc_num2-calc_num1} tries faster")
        print("Method 1 wins!")
        score_method1=score_method1+1

    elif calc_num2<calc_num1:
        # print(f"For x={x} Method 2 isolated the answer faster then method 1. {calc_num2} VS {calc_num1},{calc_num1-calc_num2} tries faster")
        print("Method 2 wins!")
        score_method2=score_method2+1
    else:
        print("It was a tie!")
        # print("it was a tie")

    total_calc_num1=total_calc_num1+calc_num1
    total_calc_num2=total_calc_num2+calc_num2
    simulation_num=simulation_num+1

print(f"========Test Results============")
print(f"1. {n}개의 경우수로 나뉠 수 있는 상황에서 {simulation_num_req}번의 시뮬레이션을 돌려보았다.")
print(f"2. Method 1.은 경우의수를 절반 씩 나눠서 if 와 else로 2분법적 논리로 나누어서 답을 찾아나선 경우이고")
print(f"3. Method 2.는 하나 하나의 경우의 수를 검증 하고 찾아낸 것이다.")
print(f"4. {simulation_num_req}의 시뮬레이션을 돌려본 결과 \"Method 1.\"이 더 적은 수의 계산으로 찾은 것은 {score_method1}번이였고 \"Method 2.\"가 더 적은 수의 계산으로 찾은 것은 {score_method2}번이였다")
print(f"5. Method 1은 {simulation_num_req}동안 총 {total_calc_num1}의 연산을 하였고 평균적으로 {total_calc_num1/simulation_num_req} 만큼 걸림")
print(f"6. Method 2은 {simulation_num_req}동안 총 {total_calc_num2}의 연산을 하였고 평균적으로 {total_calc_num2/simulation_num_req} 만큼 걸림")
print(f"7. {simulation_num_req} 동안 총 연산 차이는 {total_calc_num2-total_calc_num1} 평균적으로 두방식의 차이는 {(total_calc_num2-total_calc_num1)/simulation_num_req}이다")
