from decimal import Decimal


def root(value, root_order):
    root_value = 1 / float(root_order)
    return round(Decimal(value) ** Decimal(root_value), 3)


def minkowski_distance(x, y, order):
    return root(sum(pow(abs(a - b), order) for a, b in zip(x, y)), order)


print(minkowski_distance([1, 0, 0], [0, 1, 0], 1))
