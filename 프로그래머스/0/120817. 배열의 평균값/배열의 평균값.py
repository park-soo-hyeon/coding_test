def solution(numbers):
    answer = 0
    
    for i in range(0, len(numbers), 1):
        answer += numbers[i]
    
    return round(answer/len(numbers), 1)