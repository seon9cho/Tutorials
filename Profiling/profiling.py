# profiling.py
"""Python Essentials: Profiling.
<Name>
<Class>
<Date>
"""

# Note: for problems 1-4, you need only implement the second function listed.
# For example, you need to write max_path_fast(), but keep max_path() unchanged
# so you can do a before-and-after comparison.

import numpy as np
import time
from matplotlib import pyplot as plt

# Problem 1
def max_path(filename="triangle.txt"):
    """Find the maximum vertical path in a triangle of values."""
    with open(filename, 'r') as infile:
        data = [[int(n) for n in line.split()]
                        for line in infile.readlines()]
    def path_sum(r, c, total):
        """Recursively compute the max sum of the path starting in row r
        and column c, given the current total.
        """
        total += data[r][c]
        if r == len(data) - 1:          # Base case.
            return total
        else:                           # Recursive case.
            return max(path_sum(r+1, c,   total),   # Next row, same column
                       path_sum(r+1, c+1, total))   # Next row, next column

    return path_sum(0, 0, 0)            # Start the recursion from the top.

def max_path_fast(filename="triangle_large.txt"):
    """Find the maximum vertical path in a triangle of values."""
    with open(filename, 'r') as infile:
    	data = [[int(n) for n in line.split()]
    					for line in infile.readlines()]
    for i in range(len(data) - 2, -1, -1):
    	for j in range(len(data[i])):
    		data[i][j] += max(data[i+1][j], data[i+1][j+1])
    return data[0][0]

# Problem 2
def primes(N):
    """Compute the first N primes."""
    primes_list = []
    current = 2
    while len(primes_list) < N:
        isprime = True
        for i in range(2, current):     # Check for nontrivial divisors.
            if current % i == 0:
                isprime = False
        if isprime:
            primes_list.append(current)
        current += 1
    return primes_list

def primes_fast(N):
    """Compute the first N primes."""
    primes_list = [2]
    current = 3
    while len(primes_list) < N:
    	S = int(np.sqrt(current))
    	isprime = True
    	for i in primes_list:
            if current % i == 0:
                isprime = False
                break
            if i > S:
            	break
    	if isprime:
        	primes_list.append(current)
    	current += 2
    return primes_list

# Problem 3
def nearest_column(A, x):
    """Find the index of the column of A that is closest to x.

    Parameters:
        A ((m,n) ndarray)
        x ((m, ) ndarray)

    Returns:
        (int): The index of the column of A that is closest in norm to x.
    """
    distances = []
    for j in range(A.shape[1]):
        distances.append(np.linalg.norm(A[:,j] - x))
    return np.argmin(distances)

def nearest_column_fast(A, x):
    """Find the index of the column of A that is closest in norm to x.
    Refrain from using any loops or list comprehensions.

    Parameters:
        A ((m,n) ndarray)
        x ((m, ) ndarray)

    Returns:
        (int): The index of the column of A that is closest in norm to x.
    """
    return np.argmin(np.linalg.norm(A - x.reshape((len(x),1)), axis=0))

# Problem 4
def name_scores(filename="names.txt"):
    """Find the total of the name scores in the given file."""
    with open(filename, 'r') as infile:
        names = sorted(infile.read().replace('"', '').split(','))
    total = 0
    for i in range(len(names)):
        name_value = 0
        for j in range(len(names[i])):
            alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            for k in range(len(alphabet)):
                if names[i][j] == alphabet[k]:
                    letter_value = k + 1
            name_value += letter_value
        total += (names.index(names[i]) + 1) * name_value
    return total

def name_scores_fast(filename='names.txt'):
    """Find the total of the name scores in the given file."""
    with open(filename, 'r') as infile:
        names = sorted(infile.read().replace('"', '').split(','))
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alph_dict = {letter:index+1 for index, letter in enumerate(alphabet)}
    return sum([(i+1) * sum([alph_dict[n] for n in name]) for i, name in enumerate(names)])

# Problem 5
def fibonacci():
    """Yield the terms of the Fibonacci sequence with F_1 = F_2 = 1."""
    F_1 = 1
    F_2 = 1
    yield F_1
    yield F_2
    while True:
    	F = F_2
    	F += F_1
    	F_1 = F_2
    	F_2 = F
    	yield F


def fibonacci_digits(N=1000):
    """Return the index of the first term in the Fibonacci sequence with
    N digits.

    Returns:
        (int): The index.
    """
    for i, x in enumerate(fibonacci()):
    	if x//10**(N-1) != 0:
    		print(i+1)
    		break


# Problem 6
def prime_sieve(N):
    """Yield all primes that are less than N."""
    a = [True] * N
    a[0] = a[1] = False
    for i, isprime in enumerate(a):
    	if isprime:
    		yield(i)
    		for n in range(i*i, N, i):
    			a[n] = False

# Problem 7
def matrix_power(A, n):
    """Compute A^n, the n-th power of the matrix A."""
    product = A.copy()
    temporary_array = np.empty_like(A[0])
    m = A.shape[0]
    for power in range(1, n):
        for i in range(m):
            for j in range(m):
                total = 0
                for k in range(m):
                    total += product[i,k] * A[k,j]
                temporary_array[j] = total
            product[i] = temporary_array
    return product

from numba import jit, int64, double

@jit
def matrix_power_numba(A, n):
    """Compute A^n, the n-th power of the matrix A, with Numba optimization."""
    product = A.copy()
    temporary_array = np.empty_like(A[0])
    m = A.shape[0]
    for power in range(1, n):
        for i in range(m):
            for j in range(m):
                total = 0
                for k in range(m):
                    total += product[i,k] * A[k,j]
                temporary_array[j] = total
            product[i] = temporary_array
    return product

def prob7(n=10):
    """Time matrix_power(), matrix_power_numba(), and np.linalg.matrix_power()
    on square matrices of increasing size. Plot the times versus the size.
    """
    A = np.random.random(4).reshape((2,2))
    matrix_power_numba(A,2)
    python_matrix = []
    numba_matrix = []
    numpy_matrix = []
    size = np.array([2**i for i in range(2,8)])
    for i in size:
    	M = np.random.random(i*i).reshape((i,i))
    	t1 = time.time()
    	matrix_power(M, n)
    	t2 = time.time()
    	matrix_power_numba(M, n)
    	t3 = time.time()
    	np.linalg.matrix_power(M, n)
    	t4 = time.time()
    	python_matrix.append(t2-t1)
    	numba_matrix.append(t3-t2)
    	numpy_matrix.append(t4-t3)
    plt.ion()
    plt.loglog(size, python_matrix, label="pure python")
    plt.loglog(size, numba_matrix, label="numba")
    plt.loglog(size, numpy_matrix, label="numpy")
    plt.legend()
    plt.show()


