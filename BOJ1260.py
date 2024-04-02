# 백준 1260번 : DFS와 BFS (실버 II) original model
 
from collections import deque
from sys import stdin

input = stdin.readline

N, M, V = map(int, input().split())
graph = deque([] for i in range(N+1))
# 탐색할 행렬 생성, 0번 행 제외 1~ 행 부터 넣기 위해 range(N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]
    # 양방향 연결이기 때문에 서로의 행에 서로의 값을 추가

ds_result = deque([])
# 탐색한 번호를 저장하는 덱
bs_result = deque([V])
# V부터 탐색을 하기 때문에 결과 덱에 V를 미리 추가
c = deque([V])
# bs_result와 동일

def DFS(graph, num):
    ds_result.append(num)
    # 탐색한 번호를 결과 덱에 추가
    dsearch = graph[num]
    dsearch = sorted(dsearch)
    # 번호가 작은 곳부터 탐색하기 위해 오름차순 정렬
    for i in dsearch:
        if (i in ds_result) == False:
           # 만약 ds_result 덱에 i가 없다면
           DFS(graph, i)
           # 재귀함수
    return ds_result

while c:
    a = c.popleft()
    # pop함수는 pop한 값을 리턴하기 때문에 변수로 선언하여 pop 값 이용 가능
    bsearch = graph[a]
    bsearch = sorted(bsearch)
    for i in bsearch:
        if (i in bs_result) == False:           
            c.append(i)
            # i 리스트 중 bs_result 덱에 없는 i가 있다면 c에 추가
            # if i = [2,3,4] -> c에 2,3,4 추가 -> 2번 리스트 탐색 -> 3번 리스트 탐색 -> ... = BFS 구현
            bs_result.append(i)

print(*DFS(graph, V))
print(*bs_result)