# 백준 1620번 : 나는야 포켓몬 마스터 이다솜 (실버 IV) copy model

from sys import stdin, stdout

input = stdin.readline
print = stdout.write

N, M = map(int, input().split())

pokemon = dict()

for i in range(1, N+1):
    name = input().rstrip()
    pokemon[i] = name
    pokemon[name] = i
    # save key = num, value = name & key = name, value = num

for i in range(M):
    quest = input().rstrip()
    if quest.isdigit():
        # find number that input in string type, output type = boolean
        print('{0}\n'.format(pokemon.get(int(quest))))
    else:
        print('{0}\n'.format((pokemon.get(quest))))