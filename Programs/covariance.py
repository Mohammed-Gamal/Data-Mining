# mean (average) function
def mean(X):
    m = 0
    for i in range(0, len(X)):
        m += X[i]

    return m / len(X)


# Covariance function
def covariance(A,B):
    # find the required expected values
    AB, A_, B_ = mean([A[i]*B[i] for i in range(0, len(A))]), mean(A), mean(B)

    # evaluate the covariance, Cov(A,B) = E(A . B) - A'B'
    Cov = AB - (A_ * B_)

    return Cov


# driver
A = [2, 3, 5, 4, 6]
B = [5, 8, 10, 11, 14]

print(f'A = {A}\nB = {B}\n')
print(f'Cov(A,B) = {covariance(A,B)}')
