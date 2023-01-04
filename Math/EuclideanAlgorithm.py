def gcd_extended(first, second):
    # base condition
    if first == 0:
        return second,0,1

    gcd,x1,y1 = gcd_extended(second%first, first)

    x = y1 - (second // first) * x1
    y = x1

    return gcd, x, y


if __name__ == "__main__":
    a, b = 35, 15
    g, x, y = gcd_extended(a, b)
    print(f'gcd({a}, {b}) = {g}')
