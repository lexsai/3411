import math


def pseudo_prime(n, a):
    if math.gcd(a, n) != 1:
        return False
    if pow(a, n-1, n) != 1:
        return False
    return True


def strong_pseudo_prime(n, a):
    if not pseudo_prime(n, a):
        return False

    s = 0
    t = n - 1

    while t % 2 == 0:
        s += 1
        t //= 2

    if pow(a, t, n) == 1:
        return True

    for r in range(s):
        if pow(a, 2**r * t, n) == n - 1:
            return True

    return False


def main():
    n = 129
    options = [
        3
    ]

    strong_pseudo_prime_found = False
    for base in options:
        if strong_pseudo_prime(n, base):
            print("STRONG", base)
            strong_pseudo_prime_found = True

        if (base ** (n - 1)) % n == 1:
            print("found", base)
    if not strong_pseudo_prime_found:
        print("NO STRONG PSEUDO PRIME FOUND!!! CHECK")


if __name__ == '__main__':
    main()
