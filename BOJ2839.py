# 백준 2839번 : 설탕 배달 (실버 IV) original model

from sys import stdin, stdout
from collections import deque

input = stdin.readline
print = stdout.write

N = int(input().rstrip())
cnt_list = deque([])

for i in range(N):
    for j in range(N):
        if (5 * i) + (3 * j) == N:
            cnt_list.append(i+j)

if len(cnt_list) == 0:
    print('-1\n')
else:
    print('{0}'.format(min(cnt_list)))