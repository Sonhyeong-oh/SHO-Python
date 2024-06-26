# 백준 14492번 : 부울행렬의 부울곱 (실버 V) original model

N = int(input())
A = []
B = []

for _ in range(N):
    A.append(list(map(int, input().split())))
for _ in range(N):
    B.append(list(map(int, input().split())))

mat = []
i = 0
for i in range(N):
    # 선행 행렬의 행 고정
    alt = A[i]
    for j in range(N):
        # 후행 행렬의 열 고정
        summ = 0
        for k in range(N):
            summ += alt[k] * B[k][j]
            # 행렬 곱
        if summ > 0:
            mat.append(1)
        else:
            mat.append(0)

print(sum(mat))