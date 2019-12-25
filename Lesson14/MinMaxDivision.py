def solution(K, M, A):
    min_value = 0
    result = max_value = sum(A)
    while min_value <= max_value:
        m = (min_value + max_value) // 2
        i = 0
        j = 0
        max_sum = 0
        calc_sum = 0
        while i < K - 1 and j < len(A):
            if calc_sum + A[j] > m:
                if calc_sum > max_sum:
                    max_sum = calc_sum
                calc_sum = 0
                i += 1
            else:
                calc_sum += A[j]
                j += 1
        while j < len(A):
            calc_sum += A[j]
            j += 1
        if calc_sum > max_sum:
            max_sum = calc_sum
        if max_sum <= m:
            max_value = m - 1
        else:
            min_value = m + 1
        if max_sum < result:
            result = max_sum
    return result
