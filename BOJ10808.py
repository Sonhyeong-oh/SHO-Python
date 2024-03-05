# 백준 10808번 : 알파벳 개수 (브론즈 IV) original model

from collections import deque
word = deque(input())
word_array = [0] * 26
for i in word:
    num = ord(i) - 97
    # 아스키 코드로 변환하여 알파벳을 숫자화
    word_array[num] += 1

for i in word_array:
    print(i, end = " ")