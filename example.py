import import_target
import numpy as np

import_target.print_Hi()

A = [1,2,3]
col = np.reshape(np.array(A), (3,1))
row = np.reshape(np.array(A), (1,3))

matrix_mul = np.matmul(col, row)

print(col, row, col.shape, row.shape)
print(matrix_mul)