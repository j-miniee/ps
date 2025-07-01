n, k = map(int, input().split())
yose = [i for i in range(1, n+1)]

result = []
idx = 0

for _ in range(n):
    idx += (k-1) 
    if idx >= len(yose):
        idx = idx % len(yose)

    result.append(str(yose.pop(idx)))

print('<'+ ', '.join(result) + '>')