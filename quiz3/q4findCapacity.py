import math


def main():
    value1 = 0.6
    value2 = 0.2
    value3 = 0.5
    value4 = 0.2

    q = 1/(2**(value1/value3) + 1)

    capacity = (-q * math.log(q, 2) - (1-q) * math.log(1-q, 2) -
                value1*(q - value4)/value3 - value2)

    p = (q - value4)/value3

    print("P VALUE", p)
    print("rounded", round(p, 2))

    print("CAPACITY", capacity)
    print("rounded", round(capacity, 2))


if __name__ == '__main__':
    main()
