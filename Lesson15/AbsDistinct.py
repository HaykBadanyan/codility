def solution(A):
    count = 0
    head = 0
    prev = None
    tail = len(A) - 1
    while head <= tail:
        if abs(A[head]) > abs(A[tail]):
            index = head
            head += 1
        elif abs(A[head]) < abs(A[tail]):
            index = tail
            tail -= 1
        else:
            index = head
            head += 1
            tail -= 1
        if prev != abs(A[index]):
            prev = abs(A[index])
        else:
            continue
        count += 1
    return count
