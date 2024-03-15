# 백준 19532번 : 수학은 비대면강의입니다 (브론즈 II) original model

from sys import stdin, stdout

input = stdin.readline
print = stdout.write

a, b, c, d, e, f = map(int, input().split())

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if (a * x + b * y == c) and (d * x + e * y == f):
            print("{0} {1}".format(x, y))
            break