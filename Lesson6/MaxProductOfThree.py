from itertools import combinations


def solution(A):
    result = -1000000000
    if len(A) > 6:
        A = sorted(A)
        A = A[:3] + A[-3:]
    for items in combinations(A, 3):
        product = 1
        for i in items:
            product *= i
        if product > result:
            result = product
    return result
