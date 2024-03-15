# 백준 14125번 : 세 막대 (브론즈 III) original model

from collections import deque
from sys import stdin, stdout

input = stdin.readline
print = stdout.write

a, b, c = map(int, input().split())

len_list = deque([])
len_list.append(a)
len_list.append(b)
len_list.append(c)
len_list = sorted(len_list)

while len_list[-1] >= (len_list[-2] + len_list[-3]):
    len_list[-1] -= 1
    # 가장 큰 변이 삼각형 생성 조건에 부합할 때까지 -1

print('{0}'.format(len_list[-1] + len_list[-2] + len_list[-3]))