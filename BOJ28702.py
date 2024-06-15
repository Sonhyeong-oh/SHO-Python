# 백준 28702번 (브론즈 I) : FizzBuzz (original model)

a = input()
b = input()
c = input()

result = 0
if a.isdecimal() == True:
    result = int(a) + 3
elif b.isdecimal() == True:
    result = int(b) + 2
elif c.isdecimal() == True:
    result = int(c) + 1

if (result % 3 == 0) and (result % 5 == 0):
    print('FizzBuzz')
elif (result % 3 == 0) and (result % 5 != 0):
    print('Fizz')
elif (result % 3 != 0) and (result % 5 == 0):
    print('Buzz')
else:
    print(result)

# 문자 판별
# .isalpha() = 문자열이 알파벳인지 판별 (boolean)

# 숫자 판별
# .isdecimal() = 문자열이 int로 변환 가능한지 판별
# .isdigit() = 문자열이 숫자의 형태인지 판별 (3 위첨자 2와 같은 형태도 True 반환)
# .isnumeric() = 문자열이 숫자값을 표현하는 형태인지 (1/2 같은 형태일 떄도 True 반환)