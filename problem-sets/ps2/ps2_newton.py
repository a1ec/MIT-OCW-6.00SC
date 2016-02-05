# 6.00 Problem Set 2
#
# Successive Approximation
#
# Problem Set 2 
# Name: AC 
# Collaborators (Discussion): -
# Collaborators (Identical Solution): -
# Time: 1:30 
#

def evaluate_poly(poly, x):
    """
    Computes the polynomial function for a given value x. Returns that value.

    Example:
    >>> poly = (0.0, 0.0, 5.0, 9.3, 7.0)    # f(x) = 7x^4 + 9.3x^3 + 5x^2
    >>> x = -13
    >>> print evaluate_poly(poly, x)  # f(-13) = 7(-13)^4 + 9.3(-13)^3 + 5(-13)^2
    180339.9

    poly: tuple of numbers, length > 0
    x: number
    returns: float
    """
    y = 0.0
    i = 0
    # iterate through each item in the poly tuple
    for coeff in poly:
        y += coeff * x**i
	i += 1
    return y

def compute_deriv(poly):
    """
    Computes and returns the derivative of a polynomial function. If the
    derivative is 0, returns (0.0,).

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    # x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> print compute_deriv(poly)        # 4x^3 + 9x^2 + 35^x
    (0.0, 35.0, 9.0, 4.0)

    poly: tuple of numbers, length > 0
    returns: tuple of numbers
    """
    # iterate through poly and fill the coefficent in each tuple of the deriv
    
    if len(poly) < 2:
        return (0.0)
    coeff = []
    i = 1
    while i < len(poly):
        coeff.append(i*poly[i])
        i += 1
    return tuple(coeff)

def compute_root(poly, x_0, epsilon):
    """
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a tuple containing the root and the number of iterations required
    to get to the root.

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    #x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> x_0 = 0.1
    >>> epsilon = .0001
    >>> print compute_root(poly, x_0, epsilon)
    (0.80679075379635201, 8.0)

    poly: tuple of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: tuple (float, int)
    """

    i = 1        
    while i < 300:
        # make a better guess: x_(n+1) = x_n - f(x_n) / f'(x_n)
        x_0 = x_0 - evaluate_poly(poly, x_0) / evaluate_poly(compute_deriv(poly), x_0)
        # if guess is within tolerance
        if abs(evaluate_poly(poly, x_0)) < epsilon:
            return (x_0, i)
        i += 1
    # no root found
    print "No root found after %d iterations." % i
