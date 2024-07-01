# 백준 1822번 : 차집합 (실버 IV) original model

from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

if A-B:
    result = sorted(list(A-B))
    print(len(result))
    print(*result)
else:
    print(0)