# 백준 1475번 : 방번호 (실버 V) copy model

from collections import deque

word = deque(map(int, input()))
array = [0] * 10
# 0으로 초기화된 리스트 선언 [0, 0, ... , 0]
for i in range(len(word)):
    num = int(word[i])
    if num == 6 or num == 9:
        if array[6] <= array[9]:
            # 6보다 9가 더 많을 경우
            array[6] += 1
        else:
            # 6보다 9가 더 적을 경우
            array[9] += 1
    else: # 6, 9를 제외한 숫자일 떄
        array[num] += 1
        # num과 매칭되는 array 자리에 1을 더함
    
print(max(array))
# array 0 ~ 9 중 가장 큰 값 = 필요한 1~9 숫자 세트