import math


def main():
    p = 0.72
    radix = 3

    length = math.ceil(-math.log(p, radix))

    print("answer", length)


if __name__ == '__main__':
    main()
