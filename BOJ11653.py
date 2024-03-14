# 백준 11653번 : 소인수분해 (브론즈 I) original model

N = int(input())
num = []

for i in range(2, N+1):

    while N > 0:
        if N % i == 0:
            num.append(i)
            N = N / i
        else:
            break

print(*num, sep = "\n")