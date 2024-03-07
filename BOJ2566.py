# 백준 2566번 : 최댓값 (브론즈 III) original model

from collections import deque

matrix = deque()

for _ in range(9):
    row = list(map(int, input().split()))
    matrix.append(row)
    # 행렬 덱에 입력값을 행마다 추가
    
matrix_finder = {}

for i in matrix:
    row_finder = matrix.index(i) + 1
    # 탐색한 행의 순번을 나타냄
    column_finder = i.index(max(i)) + 1
    # 탐색한 열의 순번을 나타냄
    matrix_finder[max(i)] = (row_finder, column_finder)
    # 해당 행의 최댓값과 그 최댓값의 행, 열의 순번을 딕셔너리화

result = max(matrix_finder.keys())
# matrix_finder 딕셔너리 키 중 최댓값
print(result)
print(*matrix_finder[result])
# * = 특수문자 없이 딕셔너리의 밸류만 출력