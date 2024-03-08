# 백준 11005번 : 진법 변환 2 (브론즈 I) copy model

def convert_nota(string, base):
    rev_base = ''
    # 10진수 숫자를 변환하기 원하는 진법의 수로 나눈 결과의 나머지

    while string > 0:
        # 입력한 10진수 값이 0이 될 떄까지 시행
        string, mod = divmod(string, base)
        # divmod(a, b) => (a // b(몫), a % b(나머지))
        if mod >= 10:
        # 나머지가 10보다 커서 아라비아 숫자로 표현할 수 없다면
            mod = chr(55 + mod)
            # 아스키코드를 활용해 문자로 변환 chr(65) = 'A'
        rev_base += str(mod)
        # 결과값을 rev_base에 차례대로 추가
    return rev_base[::-1]
            # 나눗셈한 나머지를 역순으로 정렬

num, nota = map(int, input().split())
print(convert_nota(num, nota))