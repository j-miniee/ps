n = int(input())
stack, result, op = [], [], []
for _ in range(n):
    result.append(int(input()))

num = 1
idx = 0
while True:
    if stack:
        if result[idx] == stack[-1]:
            stack.pop()
            op.append('-')
            idx += 1
            continue
    
    if num > n :
        break
    stack.append(num)
    op.append('+')
    num += 1

if stack:
    print('NO')
else:
    print('\n'.join(op))