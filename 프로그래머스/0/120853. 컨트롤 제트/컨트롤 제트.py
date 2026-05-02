def solution(s):
    answer = 0
    list = s.split(' ')
    for i in range(0, len(list), 1):
        if list[i] == 'Z':
            answer -= int(list[i-1])
        else:
            answer += int(list[i])
    return answer