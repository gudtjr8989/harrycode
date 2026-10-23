from unittest import case

month=int(input("type month:"))
match month:
    case 1|3|5|7|8|10|12 :
        print(31)
    case 2:
        print(28)
    case 4|6|9|11 :
        print(30)
    case other_number: #동등 비교 하는것인대 변수를 집어 넣어주면 비교 안하고 변수에 할당하는 작업을 함
        print(f"입력하신 {other_number}월은은 문제가 없습니다")

month=int(input("type month:"))
match month:
    case 1|3|5|7|8|10|12 :
        print(31)
    case 2:
        print(28)
    case 4|6|9|11 :
        print(30)
    case _: #위 케이스가 아니라면 _바는 값에 할당이 안됨
        print(f"입력하신 {abc}월은은 문제가 없습니다")

