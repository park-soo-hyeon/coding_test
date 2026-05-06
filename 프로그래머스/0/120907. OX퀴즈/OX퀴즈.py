def solution(quiz):
    answer = []
    
    for i in quiz:
        result = i.split("=")
        if eval(result[0]) == int(result[1]):
            answer += "O"
        else:
            answer += "X"
    return answer