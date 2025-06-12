
# n_list = [[] for _ in range(s//2)]


# for list in n_list:



s = int(input())
total = 0
for n in range(s):
    total += n
    if total > s:
        break
print(n-1)

