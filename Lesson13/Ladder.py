def solution(A, B):
    max_b = max(B)
    fib = [0] * (len(A) + 2)
    fib[1] = 1 % 2 ** max_b
    for i in range(2, len(A) + 2):
        fib[i] = (fib[i - 1] + fib[i - 2]) % 2 ** max_b
    result = []
    for a, b in zip(A, B):
        result.append(fib[a+1] % 2 ** b)
    return result
