def solution(N):
    binary = f'{N:b}'
    zeros = binary.strip('0').split('1')
    max_zero_seq = max(zeros, key=lambda s: len(s))
    return len(max_zero_seq)
