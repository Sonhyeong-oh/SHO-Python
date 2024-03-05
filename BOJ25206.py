# 백준 25206번 : 너의 평점은 (실버 V) original model

from collections import deque

score_num = deque([])
# 학점 덱
score_sub = deque([])
# 과목평점 덱


def subject(a):
    if a == 'A+':
        return 4.5
    elif a == 'A0':
        return 4.0
    elif a == 'B+':
        return 3.5
    elif a == 'B0':
        return 3.0
    elif a == 'C+':
        return 2.5
    elif a == 'C0':
        return 2.0
    elif a == 'D+':
        return 1.5
    elif a == 'D0':
        return 1.0
    elif a == 'F':
        return 0
# 함수 선언을 통해 과목평점을 float형 점수로 변환

for _ in range(20):
    score = input().split()
    if score[2] == 'P':
        # 패스 과목이면 점수 계산에 포함하지 않고 점수 입력을 계속 함
        continue
    elif score[2] != 'P':
        score_num.append(float(score[1]))
        score_sub.append(subject(score[2]))

score_A = 0

for i in range(len(score_num)):
    score_A += (score_num[i] * score_sub[i])
    # 학점과 전공평점을 곱한 값을 score_A 변수에 더함

print(score_A / sum(score_num))