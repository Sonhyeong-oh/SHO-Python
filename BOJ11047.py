# 백준 11047번 : 동전 0 (실버 IV) original model

from collections import deque
from sys import stdin, stdout

input = stdin.readline
print = stdout.write

N, K = map(int, input().split())

coin_list = deque([])

for _ in range(N):
    coin_list.append(int(input().rstrip()))

coin_list = sorted(coin_list, reverse = True)

cnt = 0

for i in coin_list:
    if i <= K:
        cnt += K // i
        # K원을 동전 i원으로 나눈 몫을 카운트에 추가
        K = K % i
        # 나누고 남은 잔돈을 K로 업데이트

print('{0}'.format(cnt))