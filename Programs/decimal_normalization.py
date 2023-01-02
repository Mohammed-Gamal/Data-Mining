import numpy as np


def dec_scale(lst):
    # The maximum absolute value of A
    j = len(str(abs(np.max(lst))))

    for v in range(0, len(lst)):
        # To normalize by decimal scaling, we therefore divide each value by 10^j
        lst[v] = lst[v] / (10 ** j)  # Vi' = Vi/(10^j)

    return lst


# Values of A range from −986 to 917
A = [i for i in range(-986, 918)]

# Visualize the results
print(A)
print(dec_scale(A))
