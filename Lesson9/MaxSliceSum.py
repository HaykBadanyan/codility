def solution(A):
    max_end_sum = max_slice_sum = A[0]
    for d in A[1:]:
        max_end_sum = max(d, max_end_sum + d)
        max_slice_sum = max(max_slice_sum, max_end_sum)
    return max_slice_sum
