# 백준 3009번 : 네 번쨰 점 (브론즈 III) original model

X_list = []
Y_list = []

for _ in range(3):
    X, Y = map(int, input().split())
    X_list.append(X)
    Y_list.append(Y)

for i in X_list:
    if X_list.count(i) == 1:
        print(i, end = " ")

for j in Y_list:
    if Y_list.count(j) == 1:
        print(j)