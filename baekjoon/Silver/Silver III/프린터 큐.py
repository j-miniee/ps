from collections import deque

test = int(input())

cnt = 0
for _ in range(test):
    n, m = map(int, input().split())
    queue = deque(map(int, input().split()))

    while queue:
        if queue[0] != max(queue):
            n = queue.popleft()
            queue.append(n)
        else:
            queue.popleft()
            cnt += 1
            if m == 0:
                break
        



