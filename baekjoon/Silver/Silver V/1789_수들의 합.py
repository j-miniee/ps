s = int(input())

total = 0
cnt = 0

for i in range(1, s):
    total += i 
    cnt += 1
    if total > s:
        print(cnt-1)
        break
