# 백준 6332번 : 직각 삼각형의 두 변 (브론즈 III) original model

import math

i = 1

while 1:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    else:
        if a == -1:
            print('Triangle #%d' % i)
            try:
                cal = math.sqrt(c**2 - b**2)
                if cal != 0:
                    print('a = {:.3f}\n'.format(cal))
                else:
                    print('Impossible.\n')
            except:
                print('Impossible.\n')
        elif b == -1:
            print('Triangle #%d' % i)
            try:
                cal = math.sqrt(c**2 - a**2)
                if cal != 0:
                    print('b = {:.3f}\n'.format(cal))
                else:
                    print('Impossible.\n')
            except:
                print('Impossible.\n')
        elif c == -1:
            print('Triangle #%d' % i)
            try:
                cal = math.sqrt(a**2 + b**2)
                if cal != 0:
                    print('c = {:.3f}\n'.format(cal))
                else:
                    print('Impossible.\n')
            except:
                print('Impossible.\n')
        else:
            print('Triangle #{0}'.format(i))
            print('Impossible\n')
    i += 1