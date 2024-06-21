# 백준 13419번 : 탕수육 (브론즈 II) original model

N = int(input())
for _ in range(N):
    word = list(input())
    temp1 = []
    if len(word) % 2 != 0:
        # 단어 길이가 홀수일 경우
        for i in range(len(word)):
            try:
                temp1.append(word.pop(i))
                # pop하면 list 길이가 -1이 되고 i는 +1이 되기 때문에 i가 +2가 되는 것과 동일 
            except:
                # i가 리스트 길이보다 길어져 pop 수행 불가할 시 break
                break
            
        print(*temp1, *word, sep = '')
        print(*word, *temp1, sep = '')
    else:
        # 단어 길이가 짝수일 경우
        for i in range(len(word)):
            try:
                temp1.append(word.pop(i))
            except:
                break
        print(*temp1, sep = '')
        print(*word, sep = '')