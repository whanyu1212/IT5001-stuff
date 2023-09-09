from turtle import *


def drawTriangle(l: int) -> None:
    """Draw a triagle with each length = l
        Assume l to be an integer
        No return value

    Args:
        l (int): unit length of the triagle
    """
    for _ in range(3):
        forward(l)
        left(120)


def combine(l: int, n: int):
    # for _ in range(3):
    #     drawTriangle(100)
    #     left(120)
    # for _ in range(3):
    #     drawTriangle(l * 2)
    #     left(120)
    # for _ in range(3):
    #     drawTriangle(l * 3)
    #     left(120)
    for _ in range(3):
        for n in range(1, n + 1):
            drawTriangle(l * n)
        left(120)


if __name__ == "__main__":
    combine(100, 3)
