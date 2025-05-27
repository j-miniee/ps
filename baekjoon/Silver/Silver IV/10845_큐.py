from collections import deque

n = int(input()) # n = int(sys.stdin.readline())
queue = deque()
output = []

for _ in range(n):
    command = input() # sys.stdin.readline().strip()
    if command.startswith('push'):
        queue.append(command.split()[1])

    elif command == 'front':
        output.append(queue[0] if queue else -1)
    elif command == 'back':
        output.append(queue[-1] if queue else -1)

    elif command == 'pop':
        output.append(queue.popleft() if queue else -1)
    elif command == 'size':
        output.append(len(queue))
    elif command == 'empty':
        output.append(0 if queue else 1)

print('\n'.join(map(str, output)))
