# 백준 2606번 : 바이러스 by Breadth-First Search algorithm (실버 III) copy model

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

com = deque([1])
# 연결된 컴퓨터를 탐색하는 함수에서 탐색 기준이 되는 컴퓨터의 번호 리스트 / 1번부터 탐색
infected = [0]*(N+1)
# 바이러스가 침투했는지를 표시하기 위한 리스트를 컴퓨터 개수만큼 생성
infected[1] = 1
# 1번 컴퓨터는 이미 감염이 되어있기 때문에 1표시
# 1처리 하지 않는다면 1이 com에 추가되어 graph[1]을 또 다시 탐색하기 때문에 해줘야 함.

while com:
    c = com.popleft()
    # 현재 탐색 중인 컴퓨터 번호
    for next in graph[c]:
        print('{0}'.format(next))
        if infected[next] == 0:
            com.append(next)
            infected[next] = 1

print('{0}\n'.format(sum(infected)-1))
# 문제에서 1번 컴퓨터는 제외