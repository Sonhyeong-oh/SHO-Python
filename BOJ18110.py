# 백준 18110번 : solved.ac (실버 IV) original model

from collections import deque
from sys import stdin, stdout

write = stdout.write
input = stdin.readline

def round2(num):
    return int(num) + 1 if num - int(num) >= 0.5 else int(num)
    # math 모듈의 round 함수는 5사 5입, 따라서 4사 5입을 위함.
    # num - int(num)(소수점 내림 값) >= 0.5면 올림 (+1)

N = int(input().rstrip())

if N == 0: # 아무 의견이 없는 경우
    write('0\n')

else: # 의견이 있는 경우
    opinion = deque([])

    for _ in range(N):
        i = input().rstrip()
        opinion.append(int(i))

    outlier = round2(N * 0.15)
    trimmed = sorted(opinion)[outlier: N - outlier] 
    # 15퍼센트 절사 / [outlier: -outlier] : N <= 3 일 경우 [0: -0] -> 리스트 모든 값이 제거됨.
    trimmed_mean = round2((sum(trimmed)) / int(len(trimmed)))
        # 위의 이상값 & 아래의 이상값 제거 / 제거 후 opinion value의 개수
    write('{0}\n'.format(trimmed_mean))