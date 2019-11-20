def solution(N):
    count = 0
    index = 1
    while index * index < N:
        if N % index == 0:
            count += 2
        index += 1
    if N == index * index:
        count += 1
    return count
