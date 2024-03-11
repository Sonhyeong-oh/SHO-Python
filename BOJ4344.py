# 백준 4344번 : 평균은 넘겠지 (브론즈 I) original model

test = int(input())
for _ in range(test):
    score = list(map(int, input().split()))
    student = 0
    for i in score[1:]:
        if i > (sum(score[1:]) / score[0]):
            student += 1
    print("{:.3f}%".format(student / score[0] * 100))
    # format 안의 값을 소수점 3째자리까지 출력