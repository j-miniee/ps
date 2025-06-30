import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()

for _ in range(n):
    command = sys.stdin.readline().split()
    action = command[0]

    if action == 'push':
        queue.append(command[1])

    elif action == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)

    elif action == 'size':
        print(len(queue))

    elif action == 'empty':
        if queue:
            print(0)
        else:
            print(1)

    elif action == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)

    elif action == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)