def solution(A):
    diffs = (A[i + 1] - A[i] for i in range(len(A) - 1))
    max_end_sum = max_slice_sum = 0
    for d in diffs:
        max_end_sum = max(0, max_end_sum + d)
        max_slice_sum = max(max_slice_sum, max_end_sum)
    return max_slice_sum
