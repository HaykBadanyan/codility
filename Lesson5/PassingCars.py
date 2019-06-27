def solution(A):
    suffix_sum = [0] * (len(A) + 1)
    for i in range(len(A), 0, -1):
        suffix_sum[i-1] = suffix_sum[i] + A[i-1]
    count = 0
    for index, item in enumerate(A):
        if item == 0:
            count += suffix_sum[index+1]
        if count > 1000000000:
            return -1
    return count
