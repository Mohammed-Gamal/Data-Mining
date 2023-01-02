import numpy as np

x = [4, 6, 9, 3, 7]

x.sort()
minimum = np.min(x)
maximum = np.max(x)
range_ = maximum - minimum

print(x)
print(f'range = {maximum} - {minimum} = {range_}')
