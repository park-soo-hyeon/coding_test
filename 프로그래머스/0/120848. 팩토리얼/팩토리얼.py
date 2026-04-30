import math

def solution(n):
    answer = 1
    while True:
        if math.factorial(answer) > n:
            answer -= 1
            return answer
        answer += 1
    return answer