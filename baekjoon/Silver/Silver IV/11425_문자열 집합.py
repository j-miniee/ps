n, m = map(int, input().split())
n_arr = [input() for _ in range(n)]
m_arr = [input() for _ in range(m)]

cnt = 0
for arr in m_arr:
    if arr in n_arr:
        cnt += 1
print(cnt)
