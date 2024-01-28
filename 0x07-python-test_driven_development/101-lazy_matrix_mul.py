#!/usr/bin/python3

"""multi matrix lazy"""

import numpy
def lazy_matrix_mul(m_a, m_b):
    """
    This module multiplies 2 matrixes
    Args:
        m_a: matrix a
        m_b: matrix b
    Returns:  the daughter
    Raises:

    """

    return numpy.matmul(m_a, m_b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/101-lazy_matrix_mul.txt")
