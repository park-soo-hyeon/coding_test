def solution(polynomial):
    x, n = 0, 0
    polynomial = polynomial.split(' + ')
    for i in polynomial:
        if i.isdigit():
            n += int(i)
        else:
            x = x + 1 if i == 'x' else x + int(i[:-1])
        
    if x == 0 or n == 0:
        if x == 0 and n != 0:
            return str(n)
        elif x != 0 and n == 0:
            return (str(x) + 'x') if x != 1 else str('x')
        else:
            return str('0')
    else:
        return (str(x) + 'x' + ' + ' + str(n)) if x != 1 else ('x' + ' + ' + str(n))