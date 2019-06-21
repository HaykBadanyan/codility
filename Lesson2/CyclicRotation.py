from collections import deque


def solution(A, K):
    array = deque(A)
    array.rotate(K)
    return list(array)
