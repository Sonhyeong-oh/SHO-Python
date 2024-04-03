# 백준 2805번 : 나무 자르기 (실버 II) original model

from collections import deque
from sys import stdin, stdout

input = stdin.readline
print = stdout.write

N, M = map(int, input().split())
trees = deque(map(int, input().split()))

min = 1
Max = max(trees)

while min <= Max:
    med = (min + Max) // 2
    needs = 0
    for i in trees:
        if i > med:
            needs += i - med
    if needs >= M:
        min = (med + 1)
    else:
        Max = med - 1

print('{0}'.format(Max))