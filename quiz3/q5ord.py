def main():
    value = 4
    ord_base = 11

    for i in range(1, ord_base):
        if (value ** i) % ord_base == 1:
            print(i)
            break


if __name__ == '__main__':
    main()
