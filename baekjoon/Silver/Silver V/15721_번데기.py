a = int(input())
t = int(input())
g = int(input())

pupa = []
i = 2
while True:
    pupa.extend([0, 1, 0, 1])
    pupa.extend([0]*i + [1]*i)
    if pupa.count(g) >= t:
        break
    i += 1

cnt = 0
j = 0
while cnt < t:
    if pupa[j] == g:
        cnt += 1
    j += 1

print((j-1) % a)