def solution(dots):
    def parallel(p1, p2):
        return (abs(p2[1]-p1[1])) / (abs(p2[0]-p1[0]))
    
    if parallel(dots[0], dots[1]) == parallel(dots[2], dots[3]):
        return 1
    if parallel(dots[1], dots[2]) == parallel(dots[3], dots[0]):
        return 1
    if parallel(dots[0], dots[2]) == parallel(dots[1], dots[3]):
        return 1
    return 0