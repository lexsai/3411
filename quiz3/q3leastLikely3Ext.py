from fractions import Fraction
import math


def main():
    prob_values = [
        Fraction(5, 7),
        Fraction(2, 7),
    ]
    radix = 2
    least = 2

    ext_lengths = []
    for x in prob_values:
        for y in prob_values:
            for z in prob_values:
                ext_lengths.append(
                    (math.ceil(-math.log(x * y * z, radix)), x * y * z)
                )
    ext_lengths = sorted(ext_lengths, key=lambda x: x[0])

    print(ext_lengths)
    answer = ext_lengths[-least]

    print(f"{least} least likely l={answer[0]} p={answer[1]}")


if __name__ == '__main__':
    main()
