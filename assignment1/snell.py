from math import sin, pi, asin


def cal_incoming_angle(theta_2: float, n_1: float, n_2: float) -> float:
    """Calculate the incoming angle theta_1 in degree
       based on Snell's law: n_1 * sin(theta_1) = n_2 * sin(theta_2)

    Args:
        theta_2 (float): degree of the outgoing angle
        n_1 (float): refractive index of the first medium (water)
        n_2 (float): refractive index of the second medium (glass)

    Returns:
        float: return theta_1 in radian
    """
    theta_1 = asin(n_2 * sin(theta_2 * pi / 180) / n_1)
    theta_1_radian = theta_1 / (pi / 180)
    return theta_1_radian


ans = cal_incoming_angle(20.0, 1.33, 2.417)

print(ans)
