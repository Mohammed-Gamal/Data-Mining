import math

# Variance Method
def variance(data):
    # Number of observations
    n = len(data)

    # Mean of the data
    m = mean(data)

    # Square deviations
    deviations = [(x - m) ** 2 for x in data]

    # Variance
    variance = sum(deviations) / n

    return variance

# Standard Deviation Method
def stdev(data):
    var = variance(data)
    std_dev = math.sqrt(var)
    return std_dev

# Mean Method
def mean(data):
    return sum(data)/len(data)

# Z-Score = (x – μ) / σ
def zscore(num, data):
    return (num - mean(data)) / stdev(data)


x = 5
data = [4, 8, 6, 5, 3, 2, 8, 9, 2, 5]

z = zscore(x, data)

print(f'Z-Score is {z}')
