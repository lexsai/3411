import numpy as np

x = ["010112","021122","110022"]

vectors = [np.array([int(j) for j in y]) for y in x]

weights = []

for a in range(0,3):
    for b in range(0,3):
        for c in range(0,3):
            result = vectors[0] * a + vectors[1] * b + vectors[2] * c
            weight = 0
            for i in range(len(result)):
                if result[i] % 3 != 0:
                    weight += 1
            if weight != 0:
                weights.append(weight)

print(min(weights))