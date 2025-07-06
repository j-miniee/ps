n = int(input())

five = n // 5 
while True:
    remain = n - 5 * five 
    if remain % 2 == 0:
        print(five + remain//2)
        break
    else:
        five -= 1

    if five < 0:
        print(-1)
        break

def solution(n): # chat
    five = n // 5 

    while five >= 0:
        remain = n - 5 * five 
        if remain % 2 == 0:
            print(five + remain//2)
            break
        five -= 1

    else:
        print(-1)