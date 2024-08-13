# sympy_intro.py
"""Python Essentials: Introduction to SymPy.
<Name>
<Class>
<Date>
"""
import sympy as sy
import numpy as np
import matplotlib.pyplot as plt

# Problem 1
def prob1():
    """Return an expression for

        (2/5)e^(x^2 - y)cosh(x+y) + (3/7)log(xy + 1).

    Make sure that the fractions remain symbolic.
    """
    x, y = sy.symbols('x, y')
    return sy.Rational(2,5) * sy.exp(x**2 - y) * sy.cosh(x + y) + \
           sy.Rational(3,7) * sy.log(x*y + 1)

# Problem 2
def prob2():
    """Compute and simplify the following expression.

        product_(i=1 to 5)[ sum_(j=i to 5)[j(sin(x) + cos(x))] ]
    """
    x, i, j = sy.symbols('x, i, j')
    expr = sy.product(sy.summation(j*(sy.sin(x) + sy.cos(x)), (j, i, 5)), (i, 1, 5))
    return sy.simplify(expr)

# Problem 3
def prob3(N):
    """Define an expression for the Maclaurin series of e^x up to order N.
    Substitute in -y^2 for x to get a truncated Maclaurin series of e^(-y^2).
    Lambdify the resulting expression and plot the series on the domain
    y in [-3,3]. Plot e^(-y^2) over the same domain for comparison.
    """
    x, y, n = sy.symbols('x, y, n')
    expr = sy.summation(x**n/sy.factorial(n), (n, 0, N))
    f = sy.lambdify(y, expr.subs(x, -y**2), "numpy")
    domain = np.linspace(-2, 2, 100)
    plt.ion()
    plt.plot(domain, np.exp(-1*domain**2), label="original function")
    plt.plot(domain, f(domain), label="Maclaurin series")
    plt.legend()
    plt.show()



# Problem 4
def prob4():
    """The following equation represents a rose curve in cartesian coordinates.

    0 = 1 - [(x^2 + y^2)^(7/2) + 18x^5 y - 60x^3 y^3 + 18x y^5] / (x^2 + y^2)^3

    Construct an expression for the nonzero side of the equation and convert
    it to polar coordinates. Simplify the result, then solve it for r.
    Lambdify a solution and use it to plot x against y for theta in [0, 2pi].
    """
    theta = np.linspace(0, 2*np.pi, 200)
    x, y, r, th = sy.symbols("x, y, r, th")
    expr = 1 - ((x**2 + y**2)**sy.Rational(7,2) + 18*x**5*y \
            - 60*x**3*y**3 + 18*x*y**5)/(x**2 + y**2)**3
    expr = expr.subs({x:r*sy.cos(th), y:r*sy.sin(th)})
    expr = sy.simplify(expr)
    solutions = sy.solve(expr, r)
    r_f = sy.lambdify(th, solutions[0], "numpy")
    plt.ion()
    plt.plot(r_f(theta)*np.cos(theta), r_f(theta)*np.sin(theta))
    plt.show()

# Problem 5
def prob5():
    """Calculate the eigenvalues and eigenvectors of the following matrix.

            [x-y,   x,   0]
        A = [  x, x-y,   x]
            [  0,   x, x-y]

    Returns:
        (dict): a dictionary mapping eigenvalues (as expressions) to the
            corresponding eigenvectors (as SymPy matrices).
    """
    x, y, l = sy.symbols('x, y, l')
    A = sy.Matrix([[x-y, x, 0],
                   [x, x-y, x],
                   [0, x, x-y]])
    char_poly = sy.det(A - l*sy.eye(3))
    eig_vals = sy.solve(char_poly, l)
    eig_dict = {}
    for v in eig_vals:
        eig_dict[v] = (A - v*sy.eye(3)).nullspace()
    return eig_dict

# Problem 6
def prob6():
    """Consider the following polynomial.

        p(x) = 2*x^6 - 51*x^4 + 48*x^3 + 312*x^2 - 576*x - 100

    Plot the polynomial and its critical points. Determine which points are
    maxima and which are minima.

    Returns:
        (set): the local minima.
        (set): the local maxima.
    """
    domain = np.linspace(-5, 5, 200)
    x = sy.symbols('x')
    poly = 2*x**6 - 51*x**4 + 48*x**3 + 312*x**2 - 576*x - 100
    f = sy.lambdify(x, poly)
    _1deriv = sy.diff(poly, x)
    critical_pts = sy.solve(_1deriv, x)
    _2deriv = sy.diff(_1deriv, x)
    f_2deriv = sy.lambdify(x, _2deriv)
    loc_min = []
    loc_max = []
    for x0 in critical_pts:
        if f_2deriv(x0) > 0:
            loc_min.append(x0)
        if f_2deriv(x0) < 0:
            loc_max.append(x0)

    plt.ion()
    plt.plot(domain, f(domain))
    plt.plot(loc_min, f(np.array(loc_min)), 'ro', label="local minimum")
    plt.plot(loc_max, f(np.array(loc_max)), 'bo', label="local maximum")
    plt.legend()
    plt.show()

    return set(loc_min), set(loc_max)

# Problem 7
def prob7():
    """Calculate the integral of f(x,y,z) = (x^2 + y^2 + z^2)^2 over the
    sphere of radius r. Lambdify the resulting expression and plot the integral
    value for r in [0,3]. Return the value of the integral when r = 2.

    Returns:
        (float): the integral of f over the sphere of radius 2.
    """
    x, y, z, rh, th, ph, r = sy.symbols("x, y, z, rh, th, ph, r")
    f = (x**2 + y**2 + z**2)**2
    h = sy.Matrix([rh*sy.sin(ph)*sy.cos(th), rh*sy.sin(ph)*sy.sin(th), rh*sy.cos(ph)])
    f = f.subs({x:h[0], y:h[1], z:h[2]})
    f = sy.simplify(f)
    J = h.jacobian([rh, th, ph])
    d = -sy.simplify(J.det())
    F = sy.integrate(f*d, (rh, 0, r), (th, 0, 2*sy.pi), (ph, 0, sy.pi))
    volume_f = sy.lambdify(r, F, "numpy")
    domain = np.linspace(0, 3, 200)
    plt.ion()
    plt.plot(domain, volume_f(domain))
    plt.show()

    return F.subs(r, 2)

