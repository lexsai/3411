from math3411 import *

for m in range(0, 10):
    if m + 4 <= 2 ** m:
        print(m)

    # if 81 * (C(i, 0) + 2*(C(i, 1))) <= 3 ** i:
    #     print(i)