# 백준 1356번 : 유진수 (브론즈 I) original model

from math import *
num = input()
temp = 'NO'
if len(num) == 1:
    print('NO')
    # 한 자리 수일 경우 유진수가 될 수 없음
else:    
    for i in range(len(num)):
        multi1 = 1
        multi2 = 1

        # i를 기준으로 앞과 뒤를 나눔
        for j in num[i:]:
            multi1 = multi1 * int(j)
        for k in num[:i]:
            multi2 = multi2 * int(k)

        if multi1 == multi2:
            # 앞 구간 곱과 뒷 구간 곱이 같을 경우 반복문 탈출
            temp = 'YES'
            break

    print(temp)