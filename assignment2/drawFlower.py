from turtle import *


def drawPetal(l: int, n: int) -> None:
    """Pretty much the same as drawRegPoly
       where l is the length of each side
         and n is the number of sides
         the angle to turn will b a derived
         function from the number of sides

    Args:
        l (int): _description_
        n (int): _description_
    """
    for _ in range(n):
        forward(l)
        left(180 - (n - 2) * 180 / n)


def drawFlower(l: int, p: int, n: int) -> None:
    """draw a flower that uses drawPetal
       as a sub function. l and p will be unit length
       and the number of sides of the petal respectively
       n will be the number of petals
       The turn angle will be 360 / n since a flower is
       assumed to be round

    Args:
        l (int): unit length of the petal
        p (int): number of sides of the petal
        n (int): number of petals
    """
    for _ in range(n):
        drawPetal(l, p)
        left(360 / n)


if __name__ == "__main__":
    drawFlower(100, 8, 10)
