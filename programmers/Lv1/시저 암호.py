def solution(s, n):
    answer = ''
    
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
        else:
            if 'A' <= s[i] <= 'Z':
                code = (ord(s[i]) - ord('A') + n)% 26 + ord('A')

            elif 'a' <= s[i] <= 'z':
                code = (ord(s[i]) - ord('a') + n) % 26 + ord('a')
            
            answer += chr(code)
    
    return answer