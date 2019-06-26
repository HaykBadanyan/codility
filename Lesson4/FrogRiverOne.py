def solution(X, A):
    counter = set()
    for index, item in enumerate(A):
        counter.add(item)
        if len(counter) == X:
            return index
    return 0
