def solution(my_string):
    answer = ''
    result = list(map(str, str(my_string)))
    
    for i in result:
        if i.isupper():
            answer += i.lower()
        elif i.islower():
            answer += i.upper()
    return answer