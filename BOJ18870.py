# 백준 18870번 : 좌표압축 (실버 II) original model

from sys import stdin

input = stdin.readline

length = int(input().rstrip())
num_list = list(map(int, input().split()))
num_set = sorted(list(set(num_list)))

dic = {num_set[i] : i for i in range(len(num_set))}
# num_set의 element들을 key로, num_set은 이미 오름차순으로 정렬되어 있기 때문에 0부터 순서대로 value 부여

for i in num_list:
    print(dic[i], end = ' ')