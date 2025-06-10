n = int(input())
candy = [list(input()) for _ in range(n)]
result = 0
def check_candy():
    global result 

    for r in range(n): # 가로 맥스 카운팅
        cnt = 1
        for c in range(n-1):
            if candy[r][c] == candy[r][c+1]:
                cnt += 1
            else:
                cnt = 1
            result = max(result, cnt)
        
    for c in range(n):
        cnt = 1
        for r in range(n-1):
            if candy[r][c] == candy[r+1][c]:
                cnt += 1
            else:
                cnt = 1
            result = max(result, cnt)

    return result
    
for i in range(n):
    for j in range(n-1):
        # 가로 교체
        candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
        check_candy()
        candy[i][j+1], candy[i][j] = candy[i][j], candy[i][j+1] #원본

        # 세로 교체
        candy[j][i], candy[j+1][i] = candy[j+1][i], candy[j][i]
        check_candy()
        candy[j+1][i], candy[j][i] = candy[j][i], candy[j+1][i]

print(result)