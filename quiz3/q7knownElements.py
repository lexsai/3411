from math import gcd


def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if gcd(n, k) == 1:
            amount += 1
    return amount


def main():
    known = 6
    base = 11

    results = []

    for value in range(1, base):
        if gcd(value, base) == 1 and gcd(value, phi(base)) == 1:
            results.append(pow(known, value, base))

    results = sorted(list(set(results)))
    print(results)
    results.remove(known)
    print(results)


if __name__ == '__main__':
    main()
