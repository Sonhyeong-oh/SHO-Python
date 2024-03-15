# 백준 24267번 : 알고리즘 수업 - 알고리즘 수행 시간 6 (브론즈 II) copy model

n = int(input())
print(int((n * (n - 1) * (n - 2) / 6)))
# MenOfPassion 함수의 작동 방식 = 중복되지 않은 3수를 뽑아 조합하는 것
# = nC3 = n! / (n-3)! * 3!
print(3)