# 백준 1735번 : 분수 합 (실버 III) original model

from sys import stdin, stdout

input = stdin.readline
print = stdout.write

a, b = map(int, input().split())
c, d = map(int, input().split())
times = b * d
og_b = b
# 원래 분모 값을 저장
og_d = d
# 원래 분모 값을 저장

(b, d) = (max(b,d), min(b,d))

while d != 0:
    (b, d) = (d, (b % d))
    # 분모의 최대공약수를 구함 by 유클리드 호제법

denom = times // b
# 원래 분모의 곱 // 최대공약수 = 최소공배수

numer = a * (denom // og_b) + c * (denom // og_d)
# 통분한 분모에 맞게 분모를 바꿔 줌
(x, y) = (max(denom, numer), min(denom, numer))

while y != 0:
    (x, y) = (y, (x % y))
# 통분한 분자와 분모의 최대공약수를 구함

print('{0} {1}'.format(int(numer/x), int(denom/x)))
# 최대공약수로 약분하여 기약분수를 만듦