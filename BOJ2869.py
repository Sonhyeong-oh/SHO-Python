# 백준 2869번 : 달팽이는 올라가고 싶다 (브론즈 I) copy model

from math import *

A, B, V = map(int, input().split())

day = (V-B) / (A-B)
# 도달하는 날 = x 일 때
# A*x - B(x-1) = V
# x에 관한 식으로 정리하면 day 변수
print(ceil(day))
# 소수점이 나올 경우 올림