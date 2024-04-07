# 백준 15829번 : Hashing (브론즈 II) original model

from sys import stdin, stdout
from collections import deque

input = stdin.readline
print = stdout.write

length = int(input().rstrip())
string = deque(input().rstrip())
result = 0

for i, j in zip(range(length), range(length)):
    result += (int(ord(string[i]) - 96) * (31 ** j))
    # a를 아스키 코드로 변환하면 97
    # 따라서 ord('a')를 1로 출력하기 위해선 - 96

    # 반복문 변수 i를 2번 사용하게 되면 error 발생 (int is not iterable)
    # 따라서 i, j를 각각 선언한 후 i, j의 범위를 zip함수로 묶어줌

if result <= 5:
    print('{0}'.format(result))
else:
    print('{0}'.format(result % 1234567891))
    # 문자열의 길이가 5를 초과하면 해시 충돌을 방지하기 위해 1234567891(소수)로 나눠줌

    # *** mod = %  ex) 10 mod 3 = 1