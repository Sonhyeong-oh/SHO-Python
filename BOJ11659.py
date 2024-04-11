# 백준 11659번 : 구간 합 구하기 4 (실버 III) copy model

from sys import stdin, stdout

input = stdin.readline
print = stdout.write

N, M = map(int, input().split())
arr = list(map(int, input().split()))

sum_list = [0]
total = 0
for i in range(len(arr)):
    total += arr[i]
    sum_list.append(total)
    # ex) arr = [5 4 3 2 1] -> sum_list = [5 9 12 14 15]
    # 리스트 슬라이싱으로 접근하면(list[1:5]) 시간복잡도 O(k) -> 슬라이싱하는 개수에 비례
    # 하지만 리스트 인덱싱 = 요소 하나만 가져오면 됨. O(1) -> 시간 복잡도 면에서 인덱싱이 슬라이싱에 비해 우월 
print('{0}'.format(sum_list))
for _ in range(M):
    i, j = map(int, input().split())
    print('{0}\n'.format(sum_list[j] - sum_list[i - 1]))
    # if i = 1 -> sum_list[0] = 0 b/c sum_list already has 0