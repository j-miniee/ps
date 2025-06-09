n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

def dfs(x, y):
    if graph[x][y] == 1:
        return  False
    
    graph[x][y] = 1
    direction = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    for dx, dy in  direction:
        nx, ny = x + dx, y + dy
        if 0<= nx <n  and 0<= ny <m:
            dfs(nx, ny)
            print(f'dfs({nx}, {ny})')
    return True

frozen = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            frozen  +=  1
print(frozen)