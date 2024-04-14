# 백준 11728번 : 배열 합치기 (실버 V) copy model

from sys import stdin, stdout

input = stdin.readline
print = stdout.write

N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = A+B
# 리스트도 세트처럼 합연산 가능
C.sort()
print(' '.join(map(str, C)))
# join함수 사용을 위해선 리스트이 요소를 string으로 변환