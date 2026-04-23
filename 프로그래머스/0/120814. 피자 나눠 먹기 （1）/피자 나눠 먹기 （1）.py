def solution(n):
    answer = 1
    
    if n % 7 == 0:
        return n // 7
    
    while n // 7:
        answer += 1
        n = n - 7
        
    return answer