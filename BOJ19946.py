# 백준 19946번 : 2의 제곱수 계산하기 (브론즈 II) original model

import math
N = int(input())

while 1:
    if N % 2 != 0:
        break
    N = int(N // 2)


print(int(math.log2(N+1)))