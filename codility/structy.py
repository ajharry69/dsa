def pair_product(numbers, target_product):
    """
    Write a function, pair_product, that takes in a list and a target product as arguments. The function should return a tuple containing a pair of indices whose elements multiply to the given target. The indices returned must be unique.

    Be sure to return the indices, not the elements themselves.

    There is guaranteed to be one such pair whose product is the target.
    """
    size = len(numbers)

    fi, si = 0, 1
    while True:
        product = numbers[fi] * numbers[si]
        print(f"[{fi}]{numbers[fi]} x [{si}]{numbers[si]} =", product)
        if product == target_product:
            return (fi, si) if fi < si else (si, fi)

        if si < size - 1:
            si += 1
        elif fi < size - 2:
            fi += 1
            si = fi + 1
        else:
            break
