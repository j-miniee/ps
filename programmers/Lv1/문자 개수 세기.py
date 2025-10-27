def solution(my_string):
    answer = [0]*52

    for ch in my_string:
        if ch.isupper():
            idx = ord(ch) - ord('A')
            answer[idx] += 1
        else:
            idx = ord(ch) - ord('a') + 26
            answer[idx] += 1
            
    return answer