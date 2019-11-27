def solution(A):
    C = dict.fromkeys(A, 0)
    for i in A:
        C[i] += 1
    N = max(A)
    D = [0] * (N + 1)
    for i in A:
        D[i] += 1
    i = 1
    while i + i <= N:
        if D[i] != 0:
            k = i + i
            while k <= N:
                if D[k] != 0:
                    D[k] += C[i]
                k += i
        i += 1
    return [len(A) - D[i] for i in A]
