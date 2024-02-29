# 백준 2941번 : 크로아티아 알파벳 (실버 V) original model

sen = str(input())

def finder(sentence):
    croalpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    for i in croalpha: # 크로아티아 알파벳 리스트의 값들을 차례대로 탐색
        if i in sentence:
            sentence = sentence.replace(i, 'f')
            # 크로아티아 알파벳이 있다면 f로 변환
    print(len(sentence))
            

finder(sen)