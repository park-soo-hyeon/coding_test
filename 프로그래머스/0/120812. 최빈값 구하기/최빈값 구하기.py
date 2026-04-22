from collections import Counter

def solution(array):
    count = Counter(array)
    max_freq = max(count.values())
    modes = [k for k, v in count.items() if v == max_freq]
    return -1 if len(modes) > 1 else modes[0]