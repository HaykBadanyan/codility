from collections import deque


def solution(A, B):
    stream = []
    fishes = deque(zip(A, B))
    while fishes:
        s, d = fishes.popleft()
        while stream:
            ss, sd = stream.pop()
            if sd == 1 and d == 0:
                if ss > s:
                    stream.append((ss, sd))
                    break
                else:
                    continue
            else:
                stream.append((ss, sd))
                stream.append((s, d))
                break
        else:
            stream.append((s, d))
    return len(stream)
