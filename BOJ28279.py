# 백준 28279번 : 덱 2 (실버 IV) original model

from collections import deque
from sys import stdin, stdout

input = stdin.readline
print = stdout.write

N = int(input().rstrip())

list = deque([])

for _ in range(N):
    order = input().split()
    if order[0] == '1':
        list.appendleft(order[1])
    elif order[0] == '2':
        list.append(order[1])
    elif order[0] == '3':
        if list:
            print('{0}\n'.format(list.popleft()))
            # print(list[-1]) 후 remove(list[-1])은 시간이 오래걸림
            # list.pop()은 pop한 값을 리턴해 줌
        else:
            print('-1\n')
    elif order[0] == '4':
        if list:
            print('{0}\n'.format(list.pop()))
        else:
            print('-1\n')
    elif order[0] == '5':
        print('{0}\n'.format(len(list)))
    elif order[0] == '6':
        if list:
            print('0\n')
        else:
            print('1\n')
    elif order[0] == '8':
        if list:
            print('{0}\n'.format(list[-1]))
        else:
            print('-1\n')
    elif order[0] == '7':
        if list:
            print('{0}\n'.format(list[0]))
        else:
            print('-1\n')