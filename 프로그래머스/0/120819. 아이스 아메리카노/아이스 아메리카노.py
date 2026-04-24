def solution(money):
    answer = []
    count = 0
    while money >= 5500:
        money -= 5500
        count += 1
        
    answer = [count, money]
    return answer