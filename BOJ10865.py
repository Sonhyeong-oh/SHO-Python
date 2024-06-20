# 백준 10865번 : 친구 친구 (브론즈 III) original model

from sys import *

input = stdin.readline
print = stdout.write

a, b = map(int, input().split())
friend = [0]*(a+1)

for i in range(b):
    c, d = map(int, input().split())
    friend[c] += 1
    friend[d] += 1

for i in range(1, a+1):
    print('{0}\n'.format(friend[i]))