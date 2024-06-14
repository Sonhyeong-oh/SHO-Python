num = list(input())
cnt = 0

if len(num) <= 1:
    # 계산을 수행할 필요가 없다면 바로 판별
    if int(num[0]) % 3 == 0:
        print(0)
        print('YES')
    else:
        print(0)
        print('NO')

else:
    while len(num) != 1:
        # 한 자리 수가 될 떄까지 수행
        result = 0
        for i in num:
            result += int(i)
        cnt += 1
        num = list(str(result))

    if result % 3 == 0:
        print(cnt)
        print('YES')
    else:
        print(cnt)
        print('NO')