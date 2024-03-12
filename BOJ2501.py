# 백준 2501번 : 약수구하기 (브론즈 III) original model

N, K = map(int, input().split())

num = set()
# 중복 숫자를 방지하기 위해 set 활용

for i in range(1, N+1):
    if N % i == 0:
        num.add(N // i)

num = sorted(list(num))
try:
    print(num[K-1])
except:
    # num[K-1]에 해당하는 value가 없을 경우
    print(0)