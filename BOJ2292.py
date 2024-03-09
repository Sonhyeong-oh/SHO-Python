# 백준 2292번 : 벌집 (브론즈 II) original model

# 거쳐간 방 수 : 방의 갯수 (방의 번호) / (마지막 방 번호 // 6)
# 1 : 1
# 2 : 6 (2 ~ 7) / 1
# 3 : 12 (8 ~ 19) / 3 (1 + 2)
# 4 : 18 (20 ~ 37) / 6 (1 + 2 + 3)
# 5 : 24 (38 ~ 61) / 10 (1 + 2 + 3 + 4)      6 * sum([i for i in range(n)]) + 1
# 6 : 30 (62 ~ 91) / 15 (1 + 2 + 3 + 4 + 5)
# 7 : 36 (92 ~ 127) / 21
# 8 : 42 (128 ~ 169) / 28

num = int(input())
cnt = 1
while True:
    start = 1
    end = 6 * sum([i for i in range(cnt)]) + 1
    # cnt가 증가할 때마다 end값을 갱신
    if num == 1:
        print(1)
        break
    elif num in range(start, end+1):
        print(cnt)
        break
    else:
        start = end
        # num이 range에 속해있지 않을 경우 다음 구간을 탐색
        cnt += 1