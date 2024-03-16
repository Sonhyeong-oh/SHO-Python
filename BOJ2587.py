# 백준 2587번 : 대표값2 (브론즈 II) original model

from collections import deque
from sys import stdin, stdout

input = stdin.readline
print = stdout.write

num_list = deque([])

for _ in range(5):
    num_list.append(int(input().rstrip()))

num_list = sorted(num_list)
mean = int(sum(num_list) / len(num_list))
med = num_list[int(len(num_list) / 2)]

print('{0}\n'.format(mean))
print('{0}\n'.format(med))