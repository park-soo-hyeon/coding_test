def solution(myString):
    answer = []
    check = 0
    
    for i in range(0, len(myString), 1):
        if myString[i] == 'x':
            answer.append(myString[check:i])
            check = i+1
    if myString[check:]:
        answer.append(myString[check:])
    answer = list(filter(None, answer))
    answer.sort()
    return answer