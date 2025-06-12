def solution(k, score): # 매우 좋은 풀이!
    answer = []
    result = []

    for s in score:
        result.append(s)
        result = sorted(result)
        if len(result) > k:
            result = result[1:]
        answer.append(result[0])
    return answer

def solution1(k, score):
    answer = []
    result = score[:k]
    min_score = score[0]

    for i, s in enumerate(score):
        if i < k: # k = 3
            if min_score > s:
                min_score = s
        else:
            if s > min_score:
                result.pop(result.index(min_score))
                result.append(s)
                min_score = min(result)
                
        answer.append(min_score)
            
    return answer