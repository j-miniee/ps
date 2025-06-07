from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    # print(v, end=' ')

    for i in range(1, n+1):
        if graph[v][i] == 1 and visited[i] == False:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        # print(v, end = ' ')

        for i in range(1, n+1):
            if graph[v][i] == 1 and visited[i] == False:
                queue.append(i)
                visited[i] = True

n, m = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

cnt = 0
visited = [False] * (n+1)
for i in range(1, n+1):
    if not visited[i]:
        dfs(graph, i, visited)
        cnt += 1
print(cnt)