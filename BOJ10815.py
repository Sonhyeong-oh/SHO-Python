# 백준 10815번 : 숫자 카드 (실버 V) original model

from collections import deque
from sys import stdin, stdout

input = stdin.readline
print = stdout.write

N = int(input().rstrip())
N_list = deque(map(int, input().split()))
M = int(input().rstrip())
M_list = deque(map(int, input().split()))

N_dic = dict()
M_dic = dict()
# 실행속도 개선을 위해 dictionary형 사용

for i in N_list:
    N_dic[i] = True

for i in M_list:
    M_dic[i] = True

for i in M_dic.keys():
    if i in N_dic.keys():
        print('1 ')
    else:
        print('0 ')