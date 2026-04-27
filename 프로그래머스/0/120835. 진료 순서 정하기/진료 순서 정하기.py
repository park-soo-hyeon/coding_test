def solution(emergency):
    answer = []
    sort = sorted(emergency)
    sort.reverse()

    for i in emergency:
        answer.append(sort.index(i)+1)
        
    return answer