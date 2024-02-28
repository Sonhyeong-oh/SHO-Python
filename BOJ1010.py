# 백준 1010번 : 다리 놓기 (실버 V)

from math import *

test = int(input())

for _ in range(test):   
    N, M = map(int, input().split())
    
    if N < M:  # 두 변수의 값을 바꿈.
        temp = N
        N = M
        M = temp
    # 조합 (NCM)
    
    combi = factorial(N) / (factorial(M) * factorial(N-M))
    print(int(combi))