def solution(A):
    counter = len(A) * [0]
    for item in A:
        if item > len(A) or counter[item - 1] == 1:
            return 0
        counter[item - 1] = 1
    for item in counter:
        if item == 0:
            return 0
    return 1
