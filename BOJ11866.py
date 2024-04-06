# 백준 11866번 : 요세푸스 문제 0 (실버 V) copy model

from sys import stdin, stdout
from collections import deque

input = stdin.readline
print = stdout.write

n, k = map(int, input().split())

deq = deque([i for i in range(1, n+1)])

res = []
while len(deq) != 0:
    print('{0} {1}\n'.format(deq, res))
    # 덱의 모든 요소가 pop될 때까지
    for _ in range(k-1):
        # k번쨰 요소까지 popleft
        deq.append(deq.popleft())
    res.append(str(deq.popleft()))
    # 마지막(k번째) 요소를 res에 append

print('<'+', '.join(res)+'>')