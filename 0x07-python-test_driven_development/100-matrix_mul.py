#!/usr/bin/python3

"""multi matrix"""


def matrix_mul(m_a, m_b):
    """
    This module multiplies 2 matrixes
    Args:
        m_a: matrix a
        m_b: matrix b
    Returns:  the daughter
    Raises:

    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    a_num = False
    b_num = False
    a_rect = False
    b_rect = False
    a_emp = False
    b_emp = False

    for line in m_a:
        if not isinstance(line, list):
            raise TypeError("m_a must be a list of lists")
        if len(line) != len(m_a[0]):
            a_rect = True
        for i in line:
            if not isinstance(i, (int, float)):
                a_num = True

    for line in m_b:
        if not isinstance(line, list):
            raise TypeError("m_b must be a list of lists")
        if len(line) != len(m_b[0]):
            b_rect = True
        for i in line:
            if not isinstance(i, (int, float)):
                b_num = True
    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")
    if a_num:
        raise TypeError("m_a should contain only integers or floats")
    if b_num:
        raise TypeError("m_b should contain only integers or floats")
    if a_rect:
        raise TypeError("each row of m_a must be of the same size")
    if b_rect:
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    sol = [[] for i in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            counter = 0
            for n in range(len(m_b)):
                counter += m_a[i][n] * m_b[n][j]
            sol[i].append(counter)
    return sol


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
