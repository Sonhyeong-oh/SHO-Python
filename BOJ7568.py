# 백준 7568번 : 덩치 (실버 V) copy model

from sys import stdin, stdout
from collections import deque

input = stdin.readline
print = stdout.write

num = int(input().rstrip())
students = deque()

for _ in range(num):
    h, w = map(int, input().split())
    students.append((w, h))

for i in students:
    rank = 1
    for j in students:
        if i[0] < j[0] and i[1] < j[1]:
            # i의 키와 몸무게를 students의 모든 값과 비교, 키 또는 몸무게가 클 때마다 rank를 1씩 더함
            rank += 1
    print('{0} '.format(rank))