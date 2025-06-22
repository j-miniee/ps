n, m = map(int, input().split())
listen = [input() for _ in range(n)]
sea = [input() for _ in range(m)]

answer = list(set(listen)&set(sea))
answer.sort()

print(len(answer))
print('\n'.join(answer))
