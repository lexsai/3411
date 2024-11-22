from math import gcd


def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if gcd(n, k) == 1:
            amount += 1
    return amount


def main():
    mod = 114

    print(phi(mod))


if __name__ == '__main__':
    main()
