from math import gcd


def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if gcd(n, k) == 1:
            amount += 1
    return amount


def main():
    mod = 77
    exponent_base = 2

    print("answer 1:", phi(mod))
    print("answer 2:", pow(exponent_base, mod - phi(mod), mod))


if __name__ == '__main__':
    main()
