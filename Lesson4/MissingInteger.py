def solution(A):
    counter = [False] * (len(A) + 1)
    for item in A:
        if 0 < item <= len(A) + 1:
            counter[item - 1] = True
    for index, item in enumerate(counter):
        if item is False:
            return index + 1
