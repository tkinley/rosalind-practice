# solution.py
def hypotenuse_square(a, b):
    """Return the square of the hypotenuse given the other side lengths.

    The function accepts any real numbers for ``a`` and ``b`` and raises a
    ``ValueError`` if either value is negative.  This mirrors the mathematical
    requirement that side lengths of a triangle are non‑negative.  Using floats
    here allows the function to be used with measurements that aren't whole
    numbers (the previous implementation forced integer input via ``map(int)``,
    which raised ``ValueError`` on valid decimal input).

    Parameters
    ----------
    a : float
        Length of one side of the triangle.
    b : float
        Length of the other side of the triangle.

    Returns
    -------
    float
        The square of the hypotenuse.
    """

    if a < 0 or b < 0:
        raise ValueError("Side lengths must be non-negative")

    return a ** 2 + b ** 2

if __name__ == "__main__":
    # Read two numbers from standard input.  ``float`` is used instead of
    # ``int`` so that decimal side lengths are handled gracefully.
    a, b = map(float, input().split())

    # Compute and print a^2 + b^2.  If the result is mathematically an
    # integer, drop the trailing ``.0`` for a cleaner output.
    result = hypotenuse_square(a, b)
    print(int(result) if result.is_integer() else result)
