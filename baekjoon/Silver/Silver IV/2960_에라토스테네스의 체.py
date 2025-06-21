N, k = map(int, input().split())

num = [i for i in range(2, N+1)]

erase = 0
i = 2
while erase < k:
    for j in range(i-2, N-1):
        if num[j]!= -1 and num[j] % i == 0:
            erase += 1
            if erase == k:
                print(num[j])
                exit()
            num[j] = -1
    i += 1