def solution(n):
    square = int(n ** 0.5)
    if square*square == n :
        return 1
    return 2