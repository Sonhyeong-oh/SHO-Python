# 백준 5073번 : 삼각형과 세 변 (브론즈 III) original model

from collections import deque
from sys import stdin, stdout

input = stdin.readline
print = stdout.write

a = 1
b = 1
c = 1

while a and b and c != 0:

    len_list = deque([])

    a, b, c = map(int, input().split())

    len_list.append(a)
    len_list.append(b)
    len_list.append(c)
    len_list = sorted(len_list)

    if len_list[-1] >= (len_list[-2] + len_list[-3]):
        print('Invalid\n')
    elif a == b == c:
        print('Equilateral\n')
    elif a == b or a == c or b == c:
        print('Isosceles\n')
    elif a != b != c:
        print('Scalene\n')