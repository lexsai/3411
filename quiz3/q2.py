import math


def main():
    m_matrix = [
        [0.85, 0.2],
        [0.15, 0.8]
    ]
    p_vec = [
        4/7,
        3/7,
    ]
    symbols = 2

    assert len(m_matrix) == len(p_vec)
    result = 0
    for i in range(len(m_matrix)):
        assert len(m_matrix) == len(m_matrix[i])
        col_info = 0
        for j in range(len(m_matrix)):
            col_info += m_matrix[j][i] * -math.log(m_matrix[j][i], symbols)
        result += col_info * p_vec[i]

    print(result)
    print("rounded", round(result, 2))


if __name__ == '__main__':
    main()
