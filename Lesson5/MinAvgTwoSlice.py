def solution(A):
    prefix_sum = [0] * (len(A) + 1)
    min_avg = 10000
    min_index = 0
    for i in range(len(A)):
        prefix_sum[i+1] = prefix_sum[i] + A[i]
    for l in (2, 3):
        for i in range(len(A)-l+1):
            avg = (prefix_sum[i+l] - prefix_sum[i]) / l
            if avg < min_avg:
                min_avg = avg
                min_index = i
    return min_index
