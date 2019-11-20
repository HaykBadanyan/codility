def get_slice_sums(A):
    result = len(A) * [0]
    max_end_sum = 0
    for index, number in enumerate(A[:-1]):
        max_end_sum = max(0, max_end_sum + number)
        result[index + 1] = (max_end_sum)
    return result


def solution(A):
    main_slice = A[1:-1]
    pre = get_slice_sums(main_slice)
    rsuf = get_slice_sums(main_slice[::-1])
    return max((i + j for i, j in zip(pre, rsuf[::-1])), default=0)
