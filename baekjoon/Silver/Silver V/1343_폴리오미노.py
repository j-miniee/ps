board = input()

def check_cover(cnt):
    A_cnt = cnt // 4 
    cnt = cnt % 4 
    while A_cnt >= 0:
        if cnt % 2 == 0:
            B_cnt = cnt // 2
            word = 'A'*A_cnt*4 + 'B'*B_cnt*2
            return word
        else:
            A_cnt -= 1
    else:
        return -1

cnt = 0
result = ''
for b in board:
    if b == 'X':
        cnt += 1
    if b == '.':
        word = check_cover(cnt)
        if word == -1:
            print(-1)
            exit()
        else:
            result += word + '.'
            cnt = 0
if cnt:
    word = check_cover(cnt)
    if word == -1:
        print(-1)
        exit()
    else:
        result += word
print(result)