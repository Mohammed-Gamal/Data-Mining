from scipy.stats import chisquare

values = [250, 50, 200, 1000]
expected = [90, 210, 360, 840]

# Evaluate the chi-square
chi = chisquare(values, expected)[0]

# Display the result
print(f'Chi-square = {chi}')
