n = input()
if int(n) < 10: # while문 밖에 
    n = '0' + n

cycle = 0
new = n
while True:
    sum_digits = int(new[0]) + int(new[1])
    new = new[1] + str(sum_digits)[-1] # 여기 중요
    cycle += 1

    if new == n:
        print(cycle)
        break

def solution(n): # 처음 풀었던 풀이(str 맨 뒤 숫자 [-1]로 접근 잊지 말기)
    if int(n) < 10:
        n = '0' + n

    cycle = 0
    new = n

    while True:
        n3 = str(int(new[0]) + int(new[1]))
        if int(n3) < 10:
            n3 = '0' + n3
        new = new[1] + n3[1]
        cycle += 1
        
        if new == n:
            print(cycle)
            exit()