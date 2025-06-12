def solution(price, money, count):
    answer = sum(price *(c+1) for c in range(count))
    
    return 0 if money > answer else abs(money-answer)