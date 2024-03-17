# 백준 7785번 : 회사에 있는 사람 (실버 V) original model

from collections import deque
from sys import stdin

input = stdin.readline

N = int(input().rstrip())

employee = dict()

for _ in range(N):
    name, enle = input().split()
    employee[name] = enle

emp_list = deque([])

for i in employee.items():
    if i[1] == 'enter':
        emp_list.append(i[0])

emp_list = sorted(emp_list, reverse = True)
print(*emp_list, sep = "\n")