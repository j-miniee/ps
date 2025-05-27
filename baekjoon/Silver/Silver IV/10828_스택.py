import sys

n = int(sys.stdin.readline())
stack = []
output = []

for _ in range(n):
    command = sys.stdin.readline().strip()
    if command.startswith('push'):
        stack.append(command.split()[1])
    elif command == 'pop':
        output.append(stack.pop() if stack else -1)
    elif command == 'size':
        output.append(len(stack))
    elif command == 'empty':
        output.append(0 if stack else 1)
    elif command == 'top':
        output.append(stack[-1] if stack else -1)

print('\n'.join(map(str, output)))

