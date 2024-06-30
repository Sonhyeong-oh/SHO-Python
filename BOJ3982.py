# 백준 3982번 : Soccer Bets (실버 V) original model

N = int(input())

for _ in range(N):
    winner = dict()
    for i in range(16):
        match = list(input().split())
        if int(match[2]) > int(match[3]):
            if match[0] in winner:
                winner[match[0]] += 1
            else:
                winner[match[0]] = 1
        elif int(match[2]) < int(match[3]):
            if match[1] in winner:
                winner[match[1]] += 1
            else:
                winner[match[1]] = 1
    result = sorted(winner.items(), key=lambda x: x[1], reverse = True)
    # 밸류를 기준으로 내림차순 정렬
    print(*result[0][0], sep = "")