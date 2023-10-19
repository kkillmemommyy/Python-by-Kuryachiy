def cube_sum(n):
    a, b = 1, 1
    result = 0
    while a < n ** (1/3):
        while b < n ** (1/3):
            if a ** 3 + b ** 3 == n:
                result += 1
            b += 1
        a += 1
        b = a
    return result


