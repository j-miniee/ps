def solution(n):
    answer = ''
    
    while n:
        answer += str(n%3)
        n = n // 3
    
    n_len = len(answer)
    
    result = 0
    for i in range(n_len):
        if answer[i]:
            j = n_len-i-1
            result += int(answer[i])* (3**j)
    
    return result