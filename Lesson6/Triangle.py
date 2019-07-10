def solution(A):
    A = sorted(A)
    if len(A) < 3:
        return 0
    for i in range(len(A)-1, 1, -1):
        if A[i] + A[i-1] > A[i-2] and \
                A[i-1] + A[i-2] > A[i] and \
                A[i] + A[i-2] > A[i-1]:
            return 1
    return 0
