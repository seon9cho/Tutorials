# numpy_intro.py
"""Python Essentials: Intro to NumPy.
<Name>
Seong-Eun Cho
<Class>
Math 345
<Date>
9/12/17
"""

import numpy as np

def prob1():
    """Define the matrices A and B as arrays. Return the matrix product AB."""
    A = np.array([[3,-1,4],[1,5,-9]])
    B = np.array([[2,6,-5,3],[5,-8,9,7],[9,-3,-2,-3]])
    return A @ B

def prob2():
    """Define the matrix A as an array. Return the matrix -A^3 + 9A^2 - 15A."""
    A = np.array([[3,1,4],[1,5,9],[-5,3,1]])
    return (-1)*(A@(A@A)) + 9*(A@A) - 15*A

def prob3():
    """Define the matrices A and B as arrays. Calculate the matrix product ABA,
    change its data type to np.int64, and return it.
    """
    T = np.ones((7,7))
    A = np.triu(T)
    B = 5 * T - 6 * np.tril(T)
    C = A @ (B @ A)
    C = C.astype(np.int64)
    return C

def prob4(A):
    """Make a copy of 'A' and set all negative entries of the copy to 0.
    Return the copy.

    Example:
        >>> A = np.array([-3,-1,3])
        >>> prob4(A)
        array([0, 0, 3])
    """
    B = np.copy(A)
    mask = B < 0
    B[mask] = 0
    return B


def prob5():
    """Define the matrices A, B, and C as arrays. Return the block matrix
                                | 0 A^T I |
                                | A  0  0 |,
                                | B  0  C |
    where I is the 3x3 identity matrix and each 0 is a matrix of all zeros
    of the appropriate size.
    """
    A = np.arange(0,6).reshape(3,2).T
    B = np.tril(3*np.ones(3))
    C = (-2)*np.eye(3)
    z1 = np.zeros((A.shape[1],A.shape[1]))
    col_1 = np.vstack((z1,A,B))
    z2 = np.zeros((A.shape[0],A.shape[0]))
    z3 = np.zeros((B.shape[0],A.shape[0]))
    col_2 = np.vstack((A.T,z2,z3))
    i1 = np.eye(A.shape[1])
    z4 = np.zeros(A.shape)
    col_3 = np.vstack((i1,z4,C))
    M = np.hstack((col_1,col_2,col_3))
    return M


def prob6(A):
    """Divide each row of 'A' by the row sum and return the resulting array.

    Example:
        >>> A = np.array([[1,1,0],[0,1,0],[1,1,1]])
        >>> prob6(A)
        array([[ 0.5       ,  0.5       ,  0.        ],
               [ 0.        ,  1.        ,  0.        ],
               [ 0.33333333,  0.33333333,  0.33333333]])
    """
    B = A.sum(axis=1)
    B = B[np.newaxis].T
    return A/B


def prob7():
    """Given the array stored in grid.npy, return the greatest product of four
    adjacent numbers in the same direction (up, down, left, right, or
    diagonally) in the grid.
    """
    grid = np.load("grid.npy")
    horizontal = np.max(grid[:,:-3] * grid[:,1:-2] * grid[:,2:-1] * grid[:,3:])
    vertical = np.max(grid[:-3,:] * grid[1:-2,:] * grid[2:-1,:] * grid[3:,:])
    left_diagonal = np.max(grid[:-3,:-3] * grid[1:-2,1:-2]*grid[2:-1,2:-1]*grid[3:,3:])
    right_diagonal = np.max(grid[3:,:-3]*grid[2:-1,1:-2]*grid[1:-2,2:-1]*grid[:-3,3:])
    return int(np.max([horizontal, vertical, left_diagonal, right_diagonal]))