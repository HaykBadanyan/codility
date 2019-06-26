def solution(A):
    prefix_sum = 0
    suffix_sum = sum(A)
    min_diff = 2000
    for item in A[:-1]:
        prefix_sum += item
        suffix_sum -= item
        diff = abs(suffix_sum - prefix_sum)
        if diff < min_diff:
            min_diff = diff
    return min_diff
