def solution(A, B, C):
    planks = sorted(list(zip(A, B)))
    for i in range(len(C)):
        while True:
            l, r = 0, len(planks) - 1
            while l <= r:
                m = (l + r) // 2
                a, b = planks[m]
                if C[i] < a:
                    r = m - 1
                elif C[i] > b:
                    l = m + 1
                else:
                    planks.pop(m)
                    if not planks:
                        return i + 1
                    break
            else:
                break
    return -1
