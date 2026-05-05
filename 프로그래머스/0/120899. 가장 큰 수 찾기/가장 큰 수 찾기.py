def solution(array):
    answer = []
    maxNum = max(array)
    for i in range(0, len(array), 1):
        if array[i] == maxNum:
            answer.append(maxNum)
            answer.append(i)
    return answer