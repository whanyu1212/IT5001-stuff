from turtle import *


def drawSpiral(lineLen: int) -> None:
    """Draw a spiral with each length = lineLen
        Assume lineLen to be an integer
        minus 5 from lineLen each time
        terminate when lineLen <= 0

    Args:
        lineLen (int): unit length of the spiral
    """
    while lineLen > 0:
        forward(lineLen)
        right(90)
        lineLen -= 5


if __name__ == "__main__":
    drawSpiral(100)
