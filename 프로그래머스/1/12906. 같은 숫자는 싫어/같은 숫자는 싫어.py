from itertools import groupby

def solution(arr):
    return [key for key, group in groupby(arr)]