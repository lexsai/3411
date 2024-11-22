def main():
    h_A = 0.38
    h_B = 0.88
    i_A_B = 0.1

    h_B_A = -(i_A_B - h_B)

    h_joint_B_A = h_A + h_B_A
    print(h_joint_B_A)
    print("rounded", round(h_joint_B_A, 2))


if __name__ == '__main__':
    main()
