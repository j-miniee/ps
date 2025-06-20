n, m = map(int, input().split())

arr = [list(map(int, input().split())) for i in range(n)]

K = int(input())

for k in range(K):
    i, j, x, y = map(int, input().split())
    answer = 0
    for ny in range(i-1, x):
        for nx in range(j-1, y):
            answer += arr[ny][nx]
    print(answer)
