def rational(n, d):
    return n, d


def numer(x): return x[0]


def denom(x): return x[1]


def rational_add(x, y):
    return rational(numer(x) * denom(y) + numer(y) * denom(x),
                    denom(x) * denom(y))


def rational_repr(x):
    return "{}/{}".format(numer(x), denom(x))


if __name__ == '__main__':
    half = rational(1, 2)
    third = rational(1, 3)

    total = rational_add(half, third)

    rr = rational_repr
    print(f"{rr(half)} + {rr(third)} = {rr(total)}")
