# 백준 11399번 : ATM (실버 IV) original model

from collections import deque
from sys import stdin, stdout

input = stdin.readline
print = stdout.write

test = int(input().rstrip())
line = deque(map(int, input().split()))

line = sorted(line)

time_list = deque([])
time = 0

for i in line:
  time += i
  time_list.append(time)

print('{0}'.format(sum(time_list)))