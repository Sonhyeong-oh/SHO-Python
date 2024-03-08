# 백준 2745번 : 진법 변환 (브론즈 II) basic command

num, notation = map(str, input().split())
print(int(num, int(notation)))
# int(string, 진법) 입력 시 string에 해당하는 숫자를 10진법으로 변환