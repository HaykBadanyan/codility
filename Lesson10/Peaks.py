def solution(A):
    peaks = []
    for i in range(1, len(A) - 1):
        if A[i-1] < A[i] > A[i+1]:
            peaks.append(i)
    if not peaks:
        return 0
    i = 1
    D = []
    while i * i < len(A):
        if len(A) % i == 0:
            D.append(i)
            D.append(len(A) // i)
        i += 1
    if len(A) == i * i:
        D.append(i)
    bc = 0
    for cn in sorted(D):
        k = len(A) // cn
        i = 0
        for p in peaks:
            if i <= p < i + k:
                i += k
        if i == len(A):
            bc = cn
    return bc
