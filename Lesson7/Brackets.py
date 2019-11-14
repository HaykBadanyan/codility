def solution(S):
    if len(S) % 2 != 0:
        return 0
    open_brackets_map = {'(':')', '{': '}', '[': ']'}
    opened = []
    for s in S:
        if s in open_brackets_map:
            opened.append(s)
        else:
            if not opened or s != open_brackets_map[opened.pop()]:
                return 0
    if opened:
        return 0
    return 1
