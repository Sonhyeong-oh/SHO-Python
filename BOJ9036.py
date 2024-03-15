# 백준 9036번 : 대지 (브론즈 III) original model

from collections import deque
from sys import stdin
# 미사용 때보다 1896ms 실행속도 개선

input = stdin.readline

test = int(input().rstrip())
# 우측 개행문자 제거
print(test)

x_list = deque([])
y_list = deque([])

for _ in range(test):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

if len(x_list) <= 1:
    print(0)
else:
    len_x = max(x_list) - min(x_list)
    len_y = max(y_list) - min(y_list)
    print(len_x * len_y)
    # 정수형 출력을 위해 sys.stdout.write가 아닌 print 사용