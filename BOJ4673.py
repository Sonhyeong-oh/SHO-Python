# 백준 4673번 : 셀프 넘버 (실버 V) copy model

num_set = set(range(1, 10000))
remove_set = set() # 생성자가 있는 숫자를 추가

for num in num_set:
    for i in str(num): # 각 자릿수 별로 더하기 위해 문자로 변환
        num += int(i)
    remove_set.add(num)

self_numbers = num_set - remove_set
for self_num in sorted(self_numbers): # 오름차순으로 출력
    print(self_num)