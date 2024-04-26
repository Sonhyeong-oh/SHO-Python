# 백준 25192번 : 인사성 밝은 곰곰이 (실버 IV) original model

from sys import stdin

input = stdin.readline

N = int(input().rstrip())

array = set()

cnt = 0
enter = 0
for _ in range(N):
    word = input().rstrip()
    if word == 'ENTER':
        enter += 1
        cnt += len(array)
        array.clear()
        # ENTER 입력 시 현재 array에 있는 값들의 수를 저장 후 array를 비워 새로 들어오는 사람들을 입력
        # 재입장하는 사람들도 다시 카운트하기 위함
    else:
        if word != 'ENTER':
            array.add(word)
            # ENTER는 카운트에서 제외

cnt += len(array)
print(cnt)