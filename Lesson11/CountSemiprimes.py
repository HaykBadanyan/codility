def solution(N, P, Q):
    pA = [0] * (N + 1)
    i = 2
    while i * i <= N:
        k = i * i
        if pA[k] == 0:
            while k <= N:
                pA[k] = i
                k += i
        i += 1
    pF = [[]] * (N + 1)
    pC = [0] * (N + 1)
    for i in range(N + 1):
        x = i
        pL = []
        while pA[x] != 0:
            pL.append(pA[x])
            x //= pA[x]
        pL.append(x)
        if len(pL) == 2:
            pC[i] = pC[i - 1] + 1
        else:
            pC[i] = pC[i - 1]
    result = []
    for i, j in zip(P, Q):
        result.append(pC[j] - pC[i-1])
    return result
