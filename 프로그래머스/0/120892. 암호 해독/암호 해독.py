def solution(cipher, code):
    answer = ''
    digit_list = list(map(str, str(cipher)))
    for i in range(code-1, len(digit_list), code):
        answer += digit_list[i]
    return answer