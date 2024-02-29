# 백준 1316번 : 그룹단어 체커 (실버 V) original model

test = int(input())
cnt = 0 # 그룹 단어일 시 cnt + 1

for _ in range(test):
    str_list = []
    string = list(str(input()))

    for i in string:
        if i not in str_list: 
            str_list.append(i)
            # str_list에 중복되는 값이 없다면 알파벳을 추가
            temp = True
        elif i in str_list:
            if i == str_list[-1]:
                # 알파벳이 연속으로 나오는 경우
                str_list.append(i)
                temp = True
            elif i != str_list[-1]:
                # 알파벳이 연속적이지 않은 경우
                temp = False
                break
    if temp == True:
        # 그룹 문자일 경우 카운트를 1 더함
        cnt += 1

print(cnt)