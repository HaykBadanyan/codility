import math


def solution(A):
    peaks = []
    for i in range(1, len(A) - 1):
        if A[i-1] < A[i] > A[i+1]:
            peaks.append(i)
    if not peaks:
        return 0
    peaks_dist = peaks[-1] - peaks[0]
    k = math.ceil(peaks_dist ** 0.5)
    while k != 0:
        cnt = 1
        i = peaks[0]
        for p in peaks[1:]:
            if p - i >= k:
                i = p
                cnt += 1
                if cnt == k:
                    return k
        k -= 1
    return 1
