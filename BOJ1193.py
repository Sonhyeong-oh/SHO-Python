# 백준 1193번 : 분수찾기 (실버 V) copy model

X = int(input())
line = 1

while X > line:
    X -= line
    line += 1
# X의 위치 탐색

if line % 2 == 0:
    a = X
    b = line - X + 1
# 짝수줄인 경우 분자가 1씩 감소 -> X-=line 기작과 동일 -> 분자를 X 그대료 포기
# 분모는 1씩 증가 -> line - X를 하여 X 대비 얼마나 증가했는지 계산 + 1

elif line % 2 == 1:
    a = line - X + 1
    b = X

print(a, '/', b, sep = '')

# 0번쨰 : 1/1
# 1번쨰 : 1/2 2/1
# 2번째 : 3/1 2/2 1/3
# 3번째 : 1/4 2/3 3/2 4/1
# 짝수줄 = 분자 - 1 / 분모 + 1
# 홀수줄 = 분자 + 1 / 분모 - 1