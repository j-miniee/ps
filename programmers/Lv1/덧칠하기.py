def solution(n, m, section):
    answer = 0
    i = 0

    while i < len(section):
        start =  section[i]
        i += 1

        while i < len(section) and section[i] < start + m: 
            i += 1
        answer += 1

    return answer

def solution2(n, m, section): # 더 좋은 풀이
    cnt = 0
    last_paint = 0
    
    for s in section:
        if s > last_paint:
            cnt += 1
            last_paint = s + m -1

    return cnt