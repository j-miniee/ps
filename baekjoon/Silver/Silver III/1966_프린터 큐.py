from collections import deque

test = int(input())

for _ in range(test):
    n, m = map(int, input().split())
    queue = deque(map(int, input().split()))

    cnt = 0
    while queue:
        if queue[0] != max(queue):
            n = queue.popleft()
            queue.append(n)
        else:
            queue.popleft()
            cnt += 1

            if m == 0:
                break

        if m > 0:
            m -= 1
        else:
            m = len(queue) -1

    print(cnt)