n = int(input())
cnt = 0

n5 = n // 5

while n5 > 0:
    delivery = n - 5 * n5
    if delivery == 0 or delivery % 3 == 0:
        break
    n5 -= 1


if n % 3 != 0 and n5 <= 0:
    cnt = -1
else:
    cnt += n5
    n = n - 5 * n5
    cnt += (n//3)

print(cnt)

def solution(n): # 더 좋은 풀이
    n5 = n // 5

    while n5 >= 0:
        delivery = n - 5 * n5
        if delivery % 3 == 0:
            cnt = n5 + (delivery // 3)
            break
        n5 -= 1
    else:
        cnt = -1

    print(cnt)
solution(n)