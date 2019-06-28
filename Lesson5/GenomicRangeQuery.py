def solution(S, P, Q):
    NUCLEOTIDES = 'ACGT'
    factor = dict(zip(NUCLEOTIDES, range(1, 5)))
    prefix_sum = [dict.fromkeys(NUCLEOTIDES, 0)]
    for i, l in enumerate(S):
        prefix_sum.append(prefix_sum[i].copy())
        prefix_sum[i+1][l] += factor[l]
    results = []
    for p, q in zip(P, Q):
        for l in NUCLEOTIDES:
            if prefix_sum[q+1][l] - prefix_sum[p][l] != 0:
                results.append(factor[l])
                break
    return results
