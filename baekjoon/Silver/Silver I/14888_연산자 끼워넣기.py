n = int(input())
a = list(map(int, input().split()))
add, sub, mul, div = list(map(int, input().split())) # + - * //
max_result = -int(1e9)
min_result = int(1e9)

def dfs(add, sub, mul, div, num, idx):
    global max_result, min_result
    if idx == n:
        max_result = max(max_result, num)
        min_result = min(min_result, num)
        return 
    
    if add > 0:
        dfs(add-1, sub, mul, div, num + a[idx], idx+1)
    if sub > 0:
        dfs(add, sub-1, mul, div, num - a[idx], idx+1)
    if mul > 0:
        dfs(add, sub, mul-1, div, num * a[idx], idx+1)
    if div > 0:
        dfs(add, sub, mul, div-1, int(num / a[idx]), idx+1)

dfs(add, sub, mul, div, a[0], 1)
print(max_result)
print(min_result)
