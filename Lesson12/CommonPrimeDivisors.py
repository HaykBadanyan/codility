def gcd(a, b, res=1):
    if a == b:
        return res * a
    elif (a % 2 == 0) and (b % 2 == 0):
        return gcd(a // 2, b // 2, 2 * res)
    elif (a % 2 == 0):
        return gcd(a // 2, b, res)
    elif (b % 2 == 0):
        return gcd(a, b // 2, res)
    elif a > b:
        return gcd(a - b, b, res)
    else:
        return gcd(a, b - a, res)


def is_common(x, y):
    while y != 1 and x != y:
        x //= y
        y = gcd(y, x)
    return x == y


def solution(A, B):
    c = 0
    for a, b in zip(A, B):
        if a == b:
            c += 1
        else:
            d = gcd(a, b)
            if is_common(a, d) and is_common(b, d):
                c += 1
    return c
