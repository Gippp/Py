def pow(x, n):
    a = [1 if x != 0 else 0]
    for i in range(0, n):
        a.append(x * a[-1])
    return a
