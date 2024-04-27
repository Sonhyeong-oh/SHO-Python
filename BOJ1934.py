# 백준 1934번 : 최소공배수 (브론즈 I) original model

from sys import stdin, stdout

input = stdin.readline
print = stdout.write

num = int(input().rstrip())

# 최소 공배수 = a * b // 최대 공약수
for _ in range(num):
    a, b = map(int, input().split())
    times = a * b
    # a, b의 값을 바꾸기 전 곱한 값을 저장
    (a, b) = (max(a,b), min(a,b))
    # a,b 값을 동시에 변경
    while b != 0:
        (a, b) = (b, (a % b))
        # a,b 값을 동시에 변경
    print('{0}\n'.format(times // a))