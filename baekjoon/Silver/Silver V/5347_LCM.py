import math

n = int(input())
for _ in range(n):
    a, b = list(map(int, input().split()))
    gcd = math.gcd(a, b)
    print(a* b // gcd)