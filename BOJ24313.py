# 백준 24313번 : 알고리즘 수업 - 점근적 표기 1 (실버 V) copy model

a1, a0 = map(int, input().split())
c = int(input())
n = int(input())

if (a1 * n + a0 <= c * n) and (a1 <= c):
    # 두번쨰 조건 이유
    # 4*1 - 2 <= 2*1
    # 4*2 - 2 > 2 * 2
    # a1 > c 일 때
    # a0가 음수일 경우 n에 따라 성립되지 않을 수도 있음
    print(1)
else:
    print(0)