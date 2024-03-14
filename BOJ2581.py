# 백준 2581번 : 소수 (브론즈 II) original model

M = int(input())
N = int(input())

num_sum = []

for i in range(M, N+1):
    num_list = set()
    # 중복값 제거를 위해 set형 선택
    for j in range(1, i + 1):
        # i(M ~ N)의 숫자를 1부터 i까지로 나눠봄.
        if i % j == 0:
            # j가 i의 약수일 경우
            num_list.add(j)
            # 약수를 num_list에 추가
    if len(num_list) == 2:
        # 약수가 1과 자기 자신일 경우
        num_sum.append(i)

if len(num_sum) > 0:
    print(sum(num_sum))
    print(min(num_sum))
else:
    print(-1)