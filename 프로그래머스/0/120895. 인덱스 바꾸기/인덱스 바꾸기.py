def solution(my_string, num1, num2):
    result = list(my_string)

    a = result[num1]
    b = result[num2]

    result[num1] = b
    result[num2] = a
    
    return ''.join(result)