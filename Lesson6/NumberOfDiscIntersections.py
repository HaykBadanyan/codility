def solution(A):
    a = []
    for index, item in enumerate(A):
        a.append((index - item, False))
        a.append((index + item, True))
    a.sort()
    inter = 0
    counter = 0
    for _, ended in a:
        if ended:
            inter -= 1
            counter += inter
            if counter > 10000000:
                return -1
        else:
            inter += 1
    return counter  
