import sys
input = sys.stdin.readline

test = int(input())

for _ in range(test):
    n = int(input())
    if n < 2: 
        n = 2 # (n=1)일 때 최소값 보정

    while True:
        isdecimal = True
        for i in range(2, int(n**0.5)+ 1):
            if n % i == 0:
                isdecimal = False
                break
        if isdecimal:
            print(n)
            break
        else:
            n += 1
