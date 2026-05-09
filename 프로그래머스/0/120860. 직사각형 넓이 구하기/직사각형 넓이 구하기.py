def solution(dots):
    width = max(dots)[0] - min(dots)[0]
    height = max(dots)[1] - min(dots)[1]
    return width*height