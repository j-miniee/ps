from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    direction = [(0, -1), (0, 1), (1, 0), (-1, 0)]

    while queue:
        x, y = queue.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy

            if 0<= nx < n and 0<= ny < m and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
    
    return graph[n-1][m-1]

print(bfs(0, 0))
