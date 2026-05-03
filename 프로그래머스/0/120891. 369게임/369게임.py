def solution(order):
    answer = 0
    result = list(map(int, str(order)))
    for i in result:
        if i == 3 or i == 6 or i == 9:
            answer += 1
    return answer