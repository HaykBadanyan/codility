def get_fibs(n):
    fibs = [0, 1]
    i = 2
    fn = fibs[i - 1] + fibs[i - 2]
    while fn <= n:
        fibs.append(fn)
        i += 1
        fn = fibs[i - 1] + fibs[i - 2]
    return fibs


def solution(A):
    A.append(1)
    fibs = get_fibs(len(A))
    reps = len(A) * [-1]
    for fib in fibs[2:]:
        if A[fib-1] == 1:
            reps[fib-1] = 1
    for i in range(len(A)):
        if A[i] == 0 or reps[i] > 0:
            continue
        min_i = -1
        min_value = len(A)
        for fib in fibs[2:]:
            previous = i - fib
            if previous < 0:
                break
            if reps[previous] > 0 and reps[previous] < min_value:
                min_value = reps[previous]
                min_i = previous
        if min_i != -1:
            reps[i] = reps[min_i] + 1
    return reps[len(reps) - 1]
