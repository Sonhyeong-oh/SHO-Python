# 백준 23882번 : 알고리즘 수업 - 선택 정렬 2 (브론즈 I) copy model

n, k = map(int, input().split())
select = list(map(int, input().split()))
count = 0

for i in range(n - 1, 0, -1):
    idx = select.index(max(select[:i + 1]))
    if idx != i:
        select[idx], select[i] = select[i], select[idx]
        count += 1
        if count == k:
            print(*select)
            exit()
print(-1)