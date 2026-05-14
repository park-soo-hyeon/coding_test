def solution(num, total):
    answer = []
    first_num = (2 * total // num - num + 1) // 2
    
    for i in range(first_num, first_num+num):
        answer.append(i)
    return answer