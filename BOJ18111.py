# 백준 18111번 : 마인크래프트 (실버 II) copy model

import sys

input = sys.stdin.readline
print = sys.stdout.write

N, M, B = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]
answer = sys.maxsize
# answer에 최대 정수값을 할당
idx = 0

for floor in range(257):
    exceed_block, lack_block = 0, 0

    for i in range(N):
        for j in range(M):
            # 2차원 탐색

            if field[i][j] > floor :
                # 만약 탐색 기준값보다 배열 안의 값이 크다면
                exceed_block += field[i][j] - floor
                # 배열 안의 값을 탐색 기준값으로 빼고 그 나머지를 남는 블록으로 처리
                # 블록을 파냄
            else : 
                # 탐색 기준값 > 배열 안의 값
                lack_block += floor - field[i][j]
                # 탐색 기준값을 배열 안의 값으로 빼고 그 나머지를 부족 블록으로 처리
                # 블록을 메꿔줌

    if exceed_block + B >= lack_block :
        # 파낸 블록과 기존 갖고 있던 블록의 합이 메꾼 블록보다 많다면
        if (exceed_block * 2) + lack_block <= answer:
            # 소요 시간(= 파낸 블록 * 2초 + 메꾼 블록 * 1초)이 기존 소요시간보다 작거나 같다면
            answer = (exceed_block * 2) + lack_block
            # answer을 현재 계산한 소요 시간으로 update
            idx = floor
            # idx를 현재 계산한 층수로 update
    # 탐색 기준 층수가 1부터 시작, 따라서 소요시간이 같을 경우 가장 층수가 큰 소요시간으로 업데이트 됨.


print('{0} {1}\n'.format(answer, idx))