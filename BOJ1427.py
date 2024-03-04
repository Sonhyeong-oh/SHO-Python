# 백준 1427번 : 소트인사이드 (실버 V) original model

from collections import deque

num = list(map(int, input()))
new_num = sorted(num, reverse = True)
for i in new_num:
    print(i, end = "")

# 공통점 : 값의 크기에 따라 정렬하는 것이 아닌 부여된 순서에 따라 정렬 / .sort(reverse = True), sorted(reverse=True) 함수는 값의 크기에 따라 정렬 
# .reverse() = 객체 반환 X (None 출력) , 원형을 변경시킴, 리스트에만 사용 가능
# reversed() = 객체 반환 O (따라서 다시 리스트 또는 튜블로 변형해줘야 함.), 원형 변경 X, 리스트, 튜플, 스트링, 딕셔너리 사용 가능,