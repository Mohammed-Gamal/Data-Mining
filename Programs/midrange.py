import numpy as np

x = [4, 6, 9, 3, 7]

x.sort()
minimum = np.min(x)
maximum = np.max(x)

midrange = (maximum + minimum) / 2

print(x)
print(f'midrange = {midrange}')
