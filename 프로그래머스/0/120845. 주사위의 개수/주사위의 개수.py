def solution(box, n):
    answer = 1
    result = []
    for i in box:
        result.append(i // n)
        
    for i in result:
        answer *= i
    return answer