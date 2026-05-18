def solution(s):
    a = 0
    
    for i in s:
        if i == '(':
            a += 1
        if i == ')' and a:
            a -= 1
        elif i == ')' and a==0:
            return False
    if a==0:
        return True
    else:
        return False