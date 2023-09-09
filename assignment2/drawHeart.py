from turtle import *


def drawCurve(curve_range: int = 200) -> None:
    """Draw a curve that is slightly bigger
        than a semicircle

    Args:
        curve_range (int, optional): total units or range. Defaults to 200.
    """
    for _ in range(curve_range):
        forward(1)
        right(1)


def drawHeart(
    initial_angle: int = 140,
    intermediate_angle: int = 120,
    straight_distance: int = 100,
) -> None:
    """Combine drawCurve, straight line distance
        and angles to draw a heart filled with red

    Args:
        initial_angle (int, optional): Initial angle to turn the cursor before drawing straight line. Defaults to 140.
        intermediate_angle (int, optional): Intermediate angle to turn before drawing second curve. Defaults to 120.
        straight_distance (int, optional): Straight line distance in units. Defaults to 100.
    """
    fillcolor("red")
    begin_fill()
    left(initial_angle)
    forward(straight_distance)
    drawCurve()
    left(intermediate_angle)
    drawCurve()
    forward(straight_distance)
    end_fill()


if __name__ == "__main__":
    drawHeart()
