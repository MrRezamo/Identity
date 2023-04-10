import numpy as np


# read the dimensions of the array
x, y = (input()).split(" ")

# create the array
s = np.eye(int(x), int(y))

# legacy behavior prior to NumPy 1.14
np.set_printoptions(legacy='1.13')

# print the array
print(s)
