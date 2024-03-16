# 백준 25305번 : 커트라인 (브론즈 II) original model

from collections import deque
from sys import stdin, stdout

input = stdin.readline
print = stdout.write

num, prize = map(int, input().split())
score = deque(map(int, input().split()))

score = sorted(score, reverse = True)

print("{0}".format(score[prize - 1]))