# `Minimum`: The smallest observation in the sample.
# `1st Quartile`: The 25th percentile.
# `Median`: The middle value in the sample, also called the 50th percentile or the 2nd quartile.
# `3rd Quartile`: The 75th percentile.
# `Maximum`: The largest observation in the sample.

import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 9, 3, 6, 17, 5]
print('Before sort: ', x)

x.sort()
print('Sorted: ', x)

minimum = np.min(x)
maximum = np.max(x)
Q1 = int(((len(x) + 1) / 4) - 1)  # index
# Or  quartiles = np.percentile(x, [25, 50, 75])
median = int(np.median(x))
Q3 = int((3 * (len(x) + 1) / 4) - 1)  # index

print('Min: ', minimum)
print('Q1: ', x[Q1])
print('Median: ', median)
print('Q3: ', x[Q3])
print('Max: ', maximum)

# Plot the boxplot
plt.boxplot(x)
plt.show()
