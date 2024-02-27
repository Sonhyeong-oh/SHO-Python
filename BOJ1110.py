n = int(input())
num = n

cnt = 0

while True:
    a = num // 10 # 입력값의 10의 자리
    b = num % 10 # 입력값의 1의 자리
    c = (a+b) % 10 # 새로운 값의 1의 자리
    num = (b * 10) + c
    cnt += 1 # 시행 횟수 카운트
    if num == n:
        print(cnt)
        break