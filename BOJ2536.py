# 백준 2536번 : 색종이 (실버 V) copy model

table = [[0 for _ in range(101)] for _ in range(101)]
# 101개의 행과 열을 갖는 행렬 제작

test = int(input())

for _ in range(test):
    x, y = map(int, input().split())
    
    for row in range(x, x + 10):
        for col in range(y, y + 10):
            table[row][col] = 1
            # 입력받은 x, y 값에 따라 100cm^2의 넓이를 1로 채움

result = 0

for i in table:
    result += i.count(1)
    # table 행렬에 있는 i의 수를 카운트

print(result)