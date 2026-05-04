def solution(s):
    result = list(s)
    result.sort()
    
    return ''.join([x for x in result if result.count(x) == 1])