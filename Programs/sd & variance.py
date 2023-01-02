# Method 1
import statistics
import math

var = statistics.pvariance([4, 8, 6, 5, 3, 2, 8, 9, 2, 5])
print(f'Variance is {var}')  # 5.76

std_dev = math.sqrt(var)
print(f'Standard deviation is {std_dev}')  # 2.4


# Method 2
def variance(data):
    # Number of observations
    n = len(data)

    # Mean of the data
    mean = sum(data) / n

    # Square deviations
    deviations = [(x - mean) ** 2 for x in data]

    # Variance
    variance = sum(deviations) / n

    return variance

print(variance([4, 8, 6, 5, 3, 2, 8, 9, 2, 5])) # 5.76


def stdev(data):
    var = variance(data)
    std_dev = math.sqrt(var)
    return std_dev

print(stdev([4, 8, 6, 5, 3, 2, 8, 9, 2, 5]))  # 2.4
