from turtle import *


def drawRegPoly(L: int, n: int) -> None:
    """Draw a function to draw a regular polygon with n sides
        and each side has a length of L
        each interior angle inside the regular polygon will be
        (n-2) * 180° / n

    Args:
        L (int): Unit length of each side of the regular polygon
        n (int): The number of sides
    """

    for _ in range(n):
        forward(L)
        left(180 - (n - 2) * 180 / n)


if __name__ == "__main__":
    drawRegPoly(100, 5)
