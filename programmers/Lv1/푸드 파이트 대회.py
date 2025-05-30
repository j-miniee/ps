def solution(food):
    answer = ''
    
    for i in range(1, len(food)): 
         if food[i] >= 2:
                cnt = food[i] // 2
                for _ in range(cnt):
                    answer += str(i)

    return answer + '0' + answer[::-1]