def solution(str):
    answer = ''
    str_ord = sorted([ord(s) for s in str], reverse=True)
    
    for s in str_ord:
        answer += chr(s)
        
    return answer


def solution(s):
    return ''.join(sorted(s, reverse=True))