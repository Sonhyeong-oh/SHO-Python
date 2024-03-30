# 백준 15439번 : 베라의 패션 (브론즈 IV) original model

from collections import deque
from sys import stdin, stdout
from math import *

input = stdin.readline
print = stdout.write

N = int(input().rstrip())
if N == 1:
    num = 0
else:
    num = (factorial(N-1) / factorial(N-2)) * N
print('{0}\n'.format(int(num)))