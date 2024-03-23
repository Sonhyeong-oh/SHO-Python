# 백준 1269번 : 대칭 차집합 (실버 IV) original model

from sys import stdin, stdout

input = stdin.readline
print = stdout.write

N, M = map(int, input().split())
A = set(input().split())
B = set(input().split())

A_B = A - B
B_A = B - A
plus = len(A_B) + len(B_A)
print('{0}'.format(plus))