# 백준 2606번 : 바이러스 by Depth-First Search algorithm (실버 III) copy model

from collections import deque
from sys import stdin, stdout

input = stdin.readline
print = stdout.write

N = int(input().rstrip())
K = int(input().rstrip())

graph = deque([] for i in range(N+1))
# 컴퓨터 개수에 해당하는 만큼 연결된 컴퓨터 번호를 담을 리스트를 생성

for i in range(K):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]
    # a 컴퓨터와 b 컴퓨터는 양방향 연결

infected = [0] * (N+1)
infected[1] = 1

def dfs(v):
    infected[v] = 1
    # v에 해당하는 밸류를 1로 변경
    for next in graph[v]:
        if infected[next] == 0:
            dfs(next)
            # 1번 컴퓨터와 연결이 되어있는데 0으로 되어있다면 dfs 함수를 다시 실행하여 1로 변경

dfs(1)
print('{0}\n'.format(sum(infected)-1))
# 문제에서 1번 컴퓨터는 제외