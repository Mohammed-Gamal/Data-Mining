import numpy as np

data = [2, 5, 4, 7, 8, 5, 4, 5, 11, 13, 8, 6, 3, 8, 9]
j = 3  # number of bins

data.sort()  # sort the data
print('Data:', data)


# Partition the data into bins
def init_bins():
    c = int(len(data)/j)
    oldc = 0
    mybins = []
    temp = []
    for i in range(0, j):
        for p in range(oldc, c):
            temp.append(data[p])

        oldc = c
        c += 5
        mybins.append(temp)
        temp = []

    return mybins


bins = init_bins()
print('Bins: ', bins)


# Bins Mean
def bins_mean(bins):
    for i in range(0, len(bins)):
        bin_mean = np.mean(bins[i])
        l = len(bins[i])
        bins[i] = []

        for j in range(0, l):
            bins[i].append(bin_mean)

    return bins


bins_m = bins_mean(bins)
print('Bins mean: ', bins_m)

bins = init_bins() # reset bins

# Bins boundaries
def bins_boundary():
    bins_cpy = bins

    for i in range(0, len(bins_cpy)):
        bin_cmp = bins_m[i][0]
        bin_min = np.min(bins_cpy[i])
        bin_max = np.max(bins_cpy[i])

        for j in range(0, len(bins_cpy[i])):
            if bins_cpy[i][j] < bin_cmp:
                bins_cpy[i][j] = bin_min
            else:
                bins_cpy[i][j] = bin_max

    return bins_cpy


bins_b = bins_boundary()
print('Bins boundaries: ', bins_b)
