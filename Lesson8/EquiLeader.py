def solution(A):
    size = 0
    for item in A:
        if size == 0:
            size += 1
            value = item
        else:
            if value != item:
                size -= 1
            else:
                size += 1
    count = 0
    counts = [0] * len(A)
    for index, item in enumerate(A):
        if item == value:
            count += 1
        counts[index] = count
    result = 0
    for index in range(len(counts)):
        bcond = counts[index] > (index + 1) // 2
        econd = count - counts[index] > (len(counts) - index - 1) // 2
        if bcond and econd:
            result += 1
    return result
