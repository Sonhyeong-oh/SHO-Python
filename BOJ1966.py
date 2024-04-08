# 백준 1966번 : 프린터 큐 (실버 III) copy model

from sys import stdin, stdout
from collections import deque

input = stdin.readline
print = stdout.write

test = int(input().rstrip())
for _ in range(test):
    n, m = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    count = 0
    while queue:
        best = max(queue)
        front = queue.popleft()
        m -= 1
        # m < 0이 되면 내가 알고자 하는 위치의 문서가 인쇄

        if best == front:
            count += 1
            if m < 0:
                print('{0}\n'.format(count))
                break
                
        else:
            queue.append(front)
            # front가 덱 내에서 최댓값이 아니면 다시 덱 맨 뒤에 추가
            if m < 0:
                m = len(queue) - 1
                # m에 해당하는 value가 최댓값이 아니면 출력 불가, 따라서 m을 덱의 맨 뒷자리로 다시 할당