# 백준 12789번 : 도키도키 간식드리미 (실버 III) copy model

import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

test = int(input().rstrip())

line = deque(map(int, input().split()))
wait = deque([])
target = 1 # 간식 받는 곳으로 갈 수 있는 번호

for i in line:
    wait.append(i)
    # line에 있는 value를 하나씩 판별
    while wait and wait[-1] == target:
        # 대기 줄이 존재하면서 맨 앞의 순번이 target 순번과 같다면
        wait.pop()
        target += 1
    if len(wait) > 1 and wait[-1] > wait[-2]:
        # 대기 줄이 존재하는데 첫 번쨰 i가 target과 같지 않아 pop이 되지 못한 상황에서
        # 두 번쨰로 들어온 i가 첫 번쨰로 들어온 i보다 클 경우
        print('Sad')
        sys.exit()

if wait:
    print('Sad')
else:
    print('Nice')