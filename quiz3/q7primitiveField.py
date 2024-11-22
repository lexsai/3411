from math import gcd


def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if gcd(n, k) == 1:
            amount += 1
    return amount


def main():
    gf = 125

    print("answer:", phi(gf - 1))


if __name__ == '__main__':
    main()
