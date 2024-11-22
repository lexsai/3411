import math
from fractions import Fraction


def main():
    prob_values = [4/10, 2/10, 2/10, 1/10, 1/10]
    radix = 3

    result = 0
    for value in prob_values:
        result += value * -math.log(value, radix)

    print(result)
    print("rounded", round(result, 3))


if __name__ == '__main__':
    main()
