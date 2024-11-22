import math


def main():
    p_a1 = 0.59
    p_b1_a1 = 0.5
    p_b2_a2 = 0.61
    radix = 2

    p_a2 = 1 - p_a1
    p_b1 = p_a1 * p_b1_a1 + p_a2 * (1 - p_b2_a2)
    p_b2 = 1 - p_b1
    h_B = p_b1 * -math.log(p_b1, radix) + p_b2 * -math.log(p_b2, radix)

    print(p_a2)
    print(p_b1)
    print(p_b2)
    print(h_B)

    print("rounded values:")
    print(round(p_a2, 2))
    print(round(p_b1, 2))
    print(round(p_b2, 2))
    print(round(h_B, 2))


if __name__ == '__main__':
    main()
