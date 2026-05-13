def solution(chicken):
    answer = chicken//10
    result = chicken%10 + answer
    
    while result > 9:
        if result//10:
            answer += result//10
            result = result%10 + result//10
    return answer