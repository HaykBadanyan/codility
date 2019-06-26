def solution(N, A):
    counters = [0] * N
    max_value_effective = 0
    max_value = 0
    for i in A:
        if i != N + 1:
            if counters[i-1] < max_value_effective:
                counters[i-1] = max_value_effective
            counters[i-1] += 1
            if counters[i-1] > max_value:
                max_value = counters[i-1]
        else:
            max_value_effective = max_value
    for i in range(len(counters)):
        if counters[i] < max_value_effective:
            counters[i] = max_value_effective
    return counters
