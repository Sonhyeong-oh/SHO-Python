# 백준 1764번 : 듣보잡 (실버 IV) original model
from sys import stdin

input = stdin.readline

N, M = map(int, input().split())

dic1 = dict()
dic2 = dict()

for _ in range(N):
    dic1[input().rstrip()] = True

cnt = 0

for _ in range(M):
    name = input().rstrip()
    if name in dic1.keys():
        # input 값이 dic1에 있다면
        dic2[name] = True
        # 교집합 딕셔너리에 추가
        cnt += 1

dic2 = dict(sorted(dic2.items()))
# dic2의 키와 밸류를 키 값 기준 오름차순으로 정렬한 딕셔너리
print(cnt)
print(*dic2.keys(), sep = "\n")