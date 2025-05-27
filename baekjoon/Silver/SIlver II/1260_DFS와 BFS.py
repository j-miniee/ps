from collections import deque

def dfs(graph, n, start, visited):
    visited[start] = True
    print(start, end = ' ')

    for i in range(1, n+1):
        if graph[start][i] == 1 and visited[i] == False:
            dfs(graph, n, i, visited)

def bfs(graph, n, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end = ' ')

        for i in range(1, n+1):
            if graph[v][i] == 1 and visited[i] == False:
                queue.append(i)
                visited[i] = True

n, m, v = map(int, input().split())

graph = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

visited1 = [False] * (n+1)
visited2 = visited1.copy()

dfs(graph, n, v, visited1)
print()
bfs(graph, n, v, visited2)
