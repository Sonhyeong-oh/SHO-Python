# 백준 1463번 : 1로 만들기 (실버 III) copy model

from sys import stdin, stdout

input = stdin.readline
print = stdout.write

N = int(input().rstrip())

table = [0] * (10**6+1)
# 결과값을 저장할 테이블 생성

for i in range(2, N+1):
    table[i] = table[i-1] + 1
    # table[i-1] = 최소 연산 값으로 저장됨
    # i = (i-1) + 1, 따라서 table[i-1]에서 3rd 연산을 한 번 수행해야 하는 것이 default
    # i = 2 -> 1은 이미 1이기 때문에 연산을 0번 수행, 2는 1에서 3rd 연산을 1번 수행, 따라서 1
    if i % 2 == 0:
        table[i] = min(table[i], table[i//2]+1)
        # 2로 나누었을 때 연산 횟수는 i // 2의 최소 연산 횟수와 같아짐
        # 2로 나눈 연산을 수행했기 때문에 table[i//2]에 + 1
    if i % 3 == 0:
        table[i] = min(table[i], table[i//3]+1)

# ex)   10 -> table[10] = table[9] + 1
#       i = 9 -> 9 % 3 == 0 -> table[9] = 2 (9 // 3, 3 // 3 : 2번 수행)
#       table[10] = 3
#       10 % 2 = 5, 3 < 5 -> table[10] = 3

print('{0}'.format(table[N]))