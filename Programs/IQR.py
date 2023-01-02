# `Q1`: The 25th percentile.
# `Q3`: The 75th percentile.
#  IQR = Q3 - Q1

x = [1, 2, 9, 3, 6, 17, 5]
x.sort()
Q1, Q3 = int(((len(x) + 1) / 4) - 1), int((3 * (len(x) + 1) / 4) - 1)  # index
IQR = x[Q3] - x[Q1]

print(x)
print(f'IQR = {x[Q3]} - {x[Q1]} = {IQR}')
