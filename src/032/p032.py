def solve() -> int:
    digits = [str(d) for d in range(1, 10)]
    products: set[int] = set()
    for multiplier in range(1, 100):
        for multiplicand in range(1000 // multiplier, 10000 // multiplier):
            product = multiplier * multiplicand
            identity = f"{multiplier}{multiplicand}{product}"

            if len(identity) > 9:
                break

            if len(identity) == 9:
                if sorted(list(identity)) == digits:
                    products.add(product)
    return sum(products)
