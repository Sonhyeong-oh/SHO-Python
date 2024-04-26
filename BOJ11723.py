# 백준 11723번 : 집합 (실버 V) copy model

from sys import stdin

input = stdin.readline

N = int(input().rstrip())

A = 00000000000000000000
# 집합의 최대 길이 20

for _ in range(N):
    word = input().split()
    if word[0] == 'add':
        A |= (1 << int(word[1]))
        # 같은 자리의 A와 (1 << num) 중 하나라도 1이라면 1 반환
        # A의 word[1] 번만 1로 만들어줌
        # | = or / 대응하는 두 비트가 하나라도 1일 때 1 반환

    elif word[0] == 'remove':
        A &= ~(1 << int(word[1]))
        # ~(1 << num) : num번만 0으로 만들고 나머지는 1로 만듦.
        # 이를 A와 비교하여 같은 자리의 A와 ~(1 << num) 모두 1이면 1, 아니면 0으로 반환 
        # (~ = not) : 비트의 값을 반전하여 반환 = 0 -> 1, 1 -> 0 
        # & = and : 대응하는 두 비트가 모두 1일 때 1 반환

    elif word[0] == 'check':
        print(1 if A & (1 << int(word[1])) != 0 else 0)
        # A와 (1<<num) 이 모두 0이 아니면 1을 출력하고 아니라면 0을 출력
        # A | B (합집합), A & B (교집합), A & ~B (차집합 = A-B), A ^ B (A와 B 중 하나에만 포함되는 원소들의 집합 (A합B - A교B))

    elif word[0] == 'toggle':
        A ^= (1 << int(word[1]))
        # A와 (1 << num) 이 다르면 1 반환
        # ^ : 대응하는 두 비트가 서로 다르면 1 반환

    elif word[0] == 'empty':
        A = 0

    elif word[0] == 'all':
        A = (1<<21) - 1
        # (1<<21)을 하면 100000... 이 됨
        # 여기서 1을 뺴주면 이진법 계산에 의해 20자리가 모두 1이 됨.