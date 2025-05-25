# solution.py
def hypotenuse_square(a, b):
    """
    Calculate the square of the hypotenuse of a right triangle given the lengths of the other two sides.

    :param a: Length of one side
    :param b: Length of the other side
    :return: Square of the hypotenuse
    """
    return a**2 + b**2

if __name__ == "__main__":
    # Read two intergers from standard input
    a, b = map(int, input().split())    
    #compute and priint a^2 + b^2
    print(hypotenuse_square(a, b))
