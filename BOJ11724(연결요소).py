from collections import deque
from sys import stdin, stdout

input = stdin.readline
print = stdout.write

N, M = map(int, input().split())

graph = deque([] for i in range(N+1))

for _ in range(M):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

def DFS(num, graph):
    search = [num]
    for i in graph[num]:
        if i in search:
            num = graph[num][i]
            continue
        else:
            search.append(i)
    return search

result = deque() 
for i in range(1, N+1):
    result.append(DFS(i, graph))
print('{0}'.format(result))