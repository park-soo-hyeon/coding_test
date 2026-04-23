def solution(slice, n):
    answer = 1
    
    if n % slice == 0:
        return n // slice
    
    while n // slice:
        answer += 1
        n = n - slice
        
    return answer