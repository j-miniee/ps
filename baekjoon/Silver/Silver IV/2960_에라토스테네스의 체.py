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

def solution(n, k): # 수정 코드 ! 
    is_prime = [True]*(n+1)
    is_prime[0], is_prime[1] = False, False
    erase = 0

    for i in range(2, n+1):
        if is_prime[i]:
            for j in range(i, n+1, i): # 이 부분 좋음
                if is_prime[j]:
                    is_prime[j] = False
                    erase += 1

                    if erase == k:
                        print(j)
                        exit()