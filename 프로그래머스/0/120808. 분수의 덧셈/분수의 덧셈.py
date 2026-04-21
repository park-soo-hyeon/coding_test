import math

def solution(numer1, denom1, numer2, denom2):
    result2 = (denom1 * denom2) // math.gcd(denom1, denom2)
    result1 = numer1*(result2//denom1) + numer2*(result2//denom2)
    result3 = math.gcd(result1, result2)
    if result3:
        result1 = result1//result3
        result2 = result2//result3
    
    answer = [result1, result2]
    return answer