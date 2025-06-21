n = int(input())
big = [list(map(int, input().split())) for _ in range(n)]
result = []
for i in range(n):
    x, y = big[i]
    grade = 1
    for j in range(n):
        a, b = big[j]
        if x < a and y < b:
            grade += 1
    result.append(str(grade))

print(' '.join(result))