def main():
    h_A = 0.4
    h_B = 0.6
    h_AB = 0.7

    h_B_A = h_AB - h_A
    print(h_B - h_B_A)
    print("rounded", round(h_B - h_B_A, 2))


if __name__ == '__main__':
    main()
