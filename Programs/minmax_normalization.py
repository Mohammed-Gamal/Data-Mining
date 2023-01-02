# norm = value - min / max - min

from sklearn.preprocessing import minmax_scale

data = [1, 2, 3, 4]
norm = minmax_scale(data, feature_range=(0, 1))

print('Input data: ', data)
print('Normalized data: ', norm)
