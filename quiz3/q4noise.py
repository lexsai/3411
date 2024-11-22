import math


def main():
    p_a1 = 0.92
    p_b1_a1 = 0.86
    p_b2_a2 = 0.68

    h_B_a1 = (
        -p_b1_a1 * math.log(p_b1_a1, 2) +
        -(1 - p_b1_a1) * math.log((1 - p_b1_a1), 2)
    )
    h_B_a2 = (
        -p_b2_a2 * math.log(p_b2_a2, 2) +
        -(1 - p_b2_a2) * math.log((1 - p_b2_a2), 2)
    )
    print(h_B_a1)
    print(h_B_a2)

    h_B_A = p_a1 * h_B_a1 + (1 - p_a1) * h_B_a2
    print(h_B_A)

    print("rounded values:")

    print(round(h_B_a1, 2))
    print(round(h_B_a2, 2))
    print(round(h_B_A, 2))


if __name__ == '__main__':
    main()
