# 백준 2720번 : 세탁소 사장 동혁 (브론즈 III) original model

test = int(input())

for _ in range(test):
    money = int(input())
    quarter = 0
    dime = 0
    nickel = 0
    penny = 0
    while money != 0:
        if money >= 25:
            money = money - 25
            quarter += 1
        elif money >= 10:
            money = money - 10
            dime += 1
        elif money >= 5:
            money = money - 5
            nickel += 1
        elif money >= 1:
            money = money - 1
            penny += 1
    print(quarter, dime, nickel, penny)