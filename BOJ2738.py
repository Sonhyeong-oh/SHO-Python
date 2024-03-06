# 백준 2738번 : 행렬 덧셈 (브론즈 V) original model

from collections import deque

N, M = map(int, input().split())

matrix1 = deque() # 1번 행렬
matrix2 = deque() # 2번 행렬

for _ in range(N):
    matrix1.append(list(input().split()))
    # 한 행씩 1번 행렬에 추가
for _ in range(N):
    matrix2.append(list(input().split()))
    # 한 행씩 2번 행렬에 추가

sum_matrix = deque([])
# (1번 행렬 + 2번 행렬) 결과

for i in range(N):
    sum = []
    for j in range(M):
        sum.append(int(matrix1[i][j]) + int(matrix2[i][j]))
        # 각 행렬의 동일한 자리의 요소끼리 더함
    sum_matrix.append(sum)

for i in sum_matrix:
    print(*i) # 리스트의 요소만 출력