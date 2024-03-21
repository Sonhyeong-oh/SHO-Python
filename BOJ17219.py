# 백준 17219번 : 비밀번호 찾기 (실버 IV) original model

from sys import stdin, stdout

input = stdin.readline
print = stdout.write

list, quest = map(int, input().split())

pw_dic = dict()

for _ in range(list):
    site, pw = input().split()
    pw_dic[site] = pw
    
for _ in range(quest):
    print('{0}\n'.format(pw_dic.get(input().rstrip())))