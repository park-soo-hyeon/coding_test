def solution(sides):
    answer = 0
    a, m = 0, max(sides)
    if m:
        a = m - min(sides) + 1
        answer += 1
        while a < m:
            a += 1
            answer += 1
    
    a = sum(sides) - 1
    while a > m:
        answer += 1
        a -= 1
        
    return answer