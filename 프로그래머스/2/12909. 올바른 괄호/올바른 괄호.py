def solution(s):
    a = list()
    
    for i in s:
        if i == '(':
            a.append(i)
        
        if i == ')':
            try:
                a.pop()
            except IndexError:
                return False
    return len(a) == 0