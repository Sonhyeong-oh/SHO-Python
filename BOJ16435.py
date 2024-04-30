# 백준 16435번 : snake bird (실버 V) copy model

from sys import stdin

input = stdin.readline

N, M = map(int, input().split())

fruit = list(map(int, input().split()))
fruit.sort()

for i in range(N):
    if (M >= fruit[i]):
        M += 1
    else:
        # fruit가 M보다 더 클 경우
        break
print(M)