from math import sqrt
from typing import Tuple


def checkRoots(a: int, b: int, c: int) -> Tuple[float, float]:
    """Check if the real solution exists for this
        quadratic equation and if so, compute
        the roots

    Args:
        a (int): The coefficient of the quadratic term.
        b (int): The coefficient of the linear term.
        c (int): The constant term.

    Returns:
        Tuple[float, float]: The roots of the quadratic equation.
    """
    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        raise Exception("No real solution exists")
    elif discriminant == 0:
        return -b / (2 * a), -b / (2 * a)
    else:
        return (-b + sqrt(discriminant)) / (2 * a), (-b - sqrt(discriminant)) / (2 * a)


ans1 = checkRoots(1010, 1009, -1008)[0]
ans2 = checkRoots(1010, 1009, -1008)[1]

print(ans1, ans2)
