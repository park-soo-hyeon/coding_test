def solution(numbers, k):
    answer = 0
    count = 0
    i = 0

    while True:
        count += 1
        if count == k:
            return numbers[i]
        else:
            i += 2
            if i > len(numbers):
                i = i - len(numbers)