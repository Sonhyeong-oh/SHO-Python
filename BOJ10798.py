# 백준 10798번 : 세로읽기 (브론즈 I) original model

from collections import deque

table = deque()
max_len = 0
# table 행렬의 열 중 최대 길이

for _ in range(5):
    row = list(input())
    table.append(row)
    if len(row) > max_len:
        max_len = len(row)
        # 현재 max_len 보다 지금 삽입된 row의 길이가 길다면 max_len을 업데이트

for i in range(max_len):
    for j in range(len(table)):
        try:
            print(table[j][i], end = "")
        except:
            # table[j][i]에 해당하는 table 값이 없어 오류가 난다면 무시하고 계속 진행
            continue