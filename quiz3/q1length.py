from fractions import Fraction
import math


def main():
    prob_values = [
        Fraction(4, 10),
        Fraction(3, 10),
        Fraction(2, 10),
        Fraction(1, 10),
    ]
    radix = 2

    result = 0
    for val in prob_values:
        length = math.ceil(-math.log(val, radix))
        print(length, val)
        result += length * val

    print("answer", result)


if __name__ == '__main__':
    main()
