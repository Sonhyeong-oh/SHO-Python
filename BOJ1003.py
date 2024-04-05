# 백준 1003번 : 피보나치 함수 (실버 III) copy model

t = int(input())

for _ in range(t):
    cnt_0 = [1,0]
    # 0 = 1번 return, 1 = 0번
    cnt_1 = [0,1]
    # 0 = 0번, 1 = 1번
    n = int(input())
    if n>1:
        for i in range(n-1):
            cnt_0.append(cnt_0[-2] + cnt_0[-1])
            cnt_1.append(cnt_1[-2] + cnt_1[-1])
            # 피보나치 n에서 0, 1 호출횟수 = (피보나치 (n-1)에서 0,1 호출횟수 + 피보나치 (n-2)에서 0, 1 호출횟수)
    print(cnt_0[n], cnt_1[n])

# 주어진 숫자  0 1 2 3 4 5
# 피보나치     0 1 1 3 5 7 (n번째 피보나치 수 = (n-2)번째 주어진 숫자 + (n-1)번째 주어진 숫자)