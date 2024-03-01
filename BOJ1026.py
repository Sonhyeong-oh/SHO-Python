# 백준 1026번 : 보물 (실버 IV) original model

test = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B_dict = dict(zip([i for i in range(test)], [int(i) for i in B]))
# 0, 1, 2 순으로 key 부여 & value는 input 순서대로
sorted_B = sorted(B_dict.items(), key = lambda item:item[1], reverse = True)
# B의 key와 value를 value(item[1])의 역순(내림차순)으로 정렬

array = [] # 내림차순(value 기준)으로 정렬 후 key값을 append
for i in range(len(sorted_B)):
    array.append(sorted_B[i][0])  # value를 내림차순으로 정렬 (key = 0번이 제일 큰 값)

sorted_A = sorted(A)
A_dict = dict(zip([i for i in array], [int(i) for i in sorted_A]))
# A를 오름차순으로 정렬 후 array 값대로 key 부여
A_list = sorted(A_dict.items(), key = lambda item:item[0])
# A_dict를 오름차순(key 기준)으로 정렬

result = 0

for i in range(len(A_list)):
    times = int(A_list[i][1]) * int(B[i])
    result += times
    
print(result)