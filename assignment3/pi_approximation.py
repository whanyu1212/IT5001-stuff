def monte_carlo_pi(n: int) -> float:
    """Approximating pi using Monte Carlo method
       based on lebniz formula
       if the number is even,
       add 4/d to the sum,
       else subtract 4/d from the sum

    Args:
        n (int): the total number of terms in the series

    Returns:
        float: apprixmation of pi
    """
    sum = 0
    d = 1
    for i in range(n):
        if i % 2 == 0:
            sum += 4 / d
        else:
            sum -= 4 / d
        d += 2
    return sum


import random


def monte_carlo_pi(n: int) -> float:
    """Approximating pi by counting the number of points
        within the circle

    Args:
        n (int): number of randomly generated points

    Returns:
        float: approximated value of pi
    """
    inside_circle = 0

    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        distance = x**2 + y**2

        if distance <= 1:
            inside_circle += 1

    pi_approximation = (inside_circle / n) * 4
    return pi_approximation
