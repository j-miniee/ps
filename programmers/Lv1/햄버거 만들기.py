def solution(ingredient):
    answer = 0

    stack = []
    for value in ingredient:
        stack.append(value)
        
        if stack[-4:] == [1,2,3,1]: # 마지막 4개 확인
            answer += 1
            
            del stack[-4:] # 햄버거 만든 재료는 제거

    return answer