from fractions import Fraction
import math


def main():
    prob_values = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 6)]
    radix = 2
    most = 2

    ext_lengths = []
    for x in prob_values:
        for y in prob_values:
            for z in prob_values:
                for w in prob_values:
                    ext_lengths.append(
                        (math.ceil(
                            -math.log(x * y * z * w, radix)
                        ), x * y * z * w)
                    )

    print(ext_lengths)
    answer = ext_lengths[-most]

    print(f"{most} most long l={answer[0]} p={answer[1]}")


if __name__ == '__main__':
    main()
