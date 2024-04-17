# 백준 2669번 : 직사각형 네개의 합집합의 면적 구하기 (실버 V) original model

from sys import stdin, stdout
from collections import deque

input = stdin.readline
print = stdout.write

result = deque([0]*100 for i in range(101))
# 최대 면적 설정 (100 * 100)

for _ in range(4):
    a, b, c, d = map(int, input().split())
    for i in range(b, d):
        # y축 탐색
        for j in range(a, c):
            # x축 탐색
            if result[i][j] == 0:
                result[i][j] += 1
                # 만약 사각형 구획으로 지정되지 않은 곳이라면 지정 (1로 변경)
            
cnt = 0
for i in result:
    cnt += sum(i)
    # 사각형의 넓이
    
print('{0}'.format(cnt))