def solution(numbers):
    answer = []
    
    for i in range(0, len(numbers), 1):
        answer.append(1)
        answer[i] = numbers[i]*2
    
    return answer