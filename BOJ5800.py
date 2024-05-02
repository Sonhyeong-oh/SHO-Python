# 백준 5800번 : 성적 통계 (실버 V) original model

from sys import stdin, stdout

input = stdin.readline
print = stdout.write

case = int(input().strip())

for i in range(1, case+1):
    score = list(map(int, input().split()))
    score = score[1:]
    # 학생 수는 점수 계산에서 제외
    score = sorted(score, reverse = True)

    largest_gap = 0
    for j in range(len(score)-1):
        if score[j] - score[j+1] > largest_gap:
            largest_gap = score[j] - score[j+1]
    # 등수 별 최대 점수 차를 갱신
    
    print('Class {0}\n'.format(i))
    print('Max {0}, Min {1}, Largest gap {2}\n'.format(max(score), min(score), largest_gap))