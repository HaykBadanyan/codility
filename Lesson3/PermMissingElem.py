def solution(A):
    full_element_sum = sum(range(1, len(A) + 2))
    element_sum = sum(A)
    return full_element_sum - element_sum
