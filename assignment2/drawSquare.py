from turtle import *


def drawSquare(l: int) -> None:
    """Draw a square with each length = l
        Assume l to be an integer
        No return value

    Args:
        l (int): unit length of the square
    """
    for _ in range(4):
        forward(l)
        left(90)


if __name__ == "__main__":
    drawSquare(100)
