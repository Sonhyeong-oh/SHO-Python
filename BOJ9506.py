# 백준 9506번 : 약수들의 합 (브론즈 I) original model

num = int(input())

while num != -1:
    num_set = set()
    for i in range(1, num + 1):
        if num % i == 0:
            inte = num // i
            num_set.add(inte)

    num_set = sorted(list(num_set))
    num_set.remove(num)
    
    if num == sum(num_set):
        print("{0} = ".format(num), end = "")
        print(*num_set, sep = " + ")
        num = int(input())
    else:
        print("{0} is NOT perfect.".format(num))
        num = int(input())  