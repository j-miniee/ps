n = int(input())
C = [int(input()) for _ in range(n)]
C.sort(reverse=True) # c = sorted(c ,reverse=True)

answer = 0
for i, c in enumerate(C):
    if (i+1) % 3 == 0:
        continue
    else:
        answer += c
print(answer)



# 가장 싼거 무료라고 생각 안하고 그냥 더해서 풀었음. XXXXX
# def solution(n, c):
    # if len(c) % 3 == 0:
    #     cnt = len(c)// 3
    # else:
    #     cnt = len(c)// 3 + 1

    # bucket = []
    # for i in range(cnt):
    #     bucket.append(c[i])

    # i = cnt
    # for b in range(cnt): #2
    #     if i < n:
    #         bucket[b] += c[i]
    #     i += 2

    # print(sum(bucket))