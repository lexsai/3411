from fractions import Fraction
import math


def main():
    prob_values = [
        Fraction(3, 5),
        Fraction(2, 5)
    ]
    radix = 2
    least = 2

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
    answer = ext_lengths[least]

    print(f"{least} least long l={answer[0]} p={answer[1]}")


if __name__ == '__main__':
    main()
