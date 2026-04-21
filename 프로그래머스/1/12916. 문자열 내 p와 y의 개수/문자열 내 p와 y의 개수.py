def solution(s):
    answer = True
    y = 0
    p = 0
    
    s = s.upper()
    
    for i in range(0, len(s), 1):
        if s[i] == 'Y':
            y += 1
        if s[i] == 'P':
            p += 1
    
    if y != p:
        answer = False

    return answer