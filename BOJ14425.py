# 백준 14425번 : 문자열 집합 (실버 IV) original model
from sys import stdin, stdout

input = stdin.readline
print = stdout.write

N, M = map(int, input().split())

search = dict()
# 탐색시간 list형 >> dict형
cnt = 0

for _ in range(N):
    word = input().rstrip()
    search[word] = True

for _ in range(M):
    check = input().rstrip()
    if check in search.keys():
        cnt += 1

print('{0}'.format(cnt))