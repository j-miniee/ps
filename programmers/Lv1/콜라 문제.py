def solution(a, b, n):
    answer = 0
    
    while True:
        blank = (n // a)  * b
        answer += blank 
        n = (n % a + blank )
        if n < a:
            break
    
    return answer