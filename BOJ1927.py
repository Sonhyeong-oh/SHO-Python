# 백준 1927번 : 최소 힙 (실버 II) original model

from queue import PriorityQueue
# 우선순위 큐 사용을 위한 파이썬 내장함수 PriorityQueue 호출 
# 리스트 시간복잡도 : input = O(1), pop = O(N)
# 힙(우선순위 큐) = input, pop = O(logN)
from sys import stdin, stdout

input = stdin.readline
print = stdout.write

N = int(input().rstrip())
que = PriorityQueue()
# 최대크기 제한 = PriorityQueue(maxsize=number)

for _ in range(N):
    word = int(input().rstrip())
    if word == 0:
        if que.empty() == True:
            # 힙이 비어있다면
            print('0\n')
        else:
            print("{0}\n".format(que.get()))
            # get = pop, pop과 마찬가지로 get한 value를 리턴
            # 우선순위 큐는 자료를 put 순서와 상관없이 오름차순 정렬, get도 작은 숫자 순서대로 반환
    else:
        que.put(word)
        # put = append

# len(que) = que.qsize()
# que.empty() -> print by boolean
# que.full() -> que가 maxsize와 일치한다면 True 아니면 False