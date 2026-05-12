def solution(score):
    answer = []
    for i in score:
        answer.append((i[0]+i[1])/2)
    
    a = sorted(answer, reverse = True)
    ranks = [a.index(s) + 1 for s in answer]
    return ranks