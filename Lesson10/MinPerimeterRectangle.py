def solution(N):
    index = 1
    perimeters = []
    while index * index < N:
        if N % index == 0:
            perimeters.append(2 * (index + N // index))
        index += 1
    if N == index * index:
        perimeters.append(2 * (index + index))
    return min(perimeters)
