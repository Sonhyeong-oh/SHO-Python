# 백준 5086번 : 배수와 약수 (브론즈 III) original model

a, b = map(int, input().split())

while a or b != 0:
    if b % a == 0:
        print('factor')
    elif a % b == 0:
        print('multiple')
    else:
        print('neither')
    a, b = map(int, input().split())