# 백준 4134번 : 다음 소수 (실버 IV) original model

from sys import stdin, stdout

input = stdin.readline
print = stdout.write

num = int(input().rstrip())

def prime(N):
    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
            return False
    return True
# 소수 판별을 위해 2부터 sqrt(N) 까지 나눠봄

for _ in range(num):
    N = int(input().rstrip())
    if N == 1 or N == 0:
        print('{0}\n'.format(2))
    # 0과 1은 소수가 아니므로 바로 2를 출력
    else:        
        while prime(N) == False:
            N += 1
        # prime 함수의 리턴값이 True일 때까지 N += 1하여 탐색
        print('{0}\n'.format(N))