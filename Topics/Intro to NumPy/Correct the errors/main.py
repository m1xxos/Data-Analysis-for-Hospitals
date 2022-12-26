import numpy as np

arr = np.array([[1, 5, 6],
                [0, 5, 7],
                [9, 0, 3]])
for i in range(-3, 4):
    x = (i**3) + 3*i**2 - i - 3
    print(x)
