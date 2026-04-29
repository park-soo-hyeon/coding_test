def solution(num_list, n):
    rows = len(num_list)//n
    cols = n
    a = 0
    
    answer = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            answer[i][j] += num_list[a]
            a += 1
    return answer
