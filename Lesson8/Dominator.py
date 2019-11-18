def solution(A):
    size = 0
    for i in A:
        if size == 0:
            size += 1
            value = i
        else:
            if value != i:
                size -= 1
            else:
                size += 1
    if size == 0:
        return -1
    candidate = value
    count = 0
    for index, item in enumerate(A):
        if item == candidate:
            count += 1
            if count > len(A) // 2:
                return index
    return -1
