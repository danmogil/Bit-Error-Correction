from numpy import dtype, matmul, ndarray, transpose, empty, append, vstack, array, concatenate
from math import log2

c = ''
a = [1, 1, 1]
b = [0, 0, 0]
c += str(matmul(a, vstack(b)).item())
print(c)