# def calculate_factorial(n):
#     if n < 0:
#         return None
#     elif n == 0:
#         return 1
#     else:
#         result = 1
#         for i in range(1, n + 1):
#             result *= i
#         return result

# def nChooseK(n, k):
#     return calculate_factorial(n) / (calculate_factorial(k) * calculate_factorial(n - k))


def nChooseK(n: int, k: int) -> int:
    """formula for n choose k


    Args:
        n (int): Total number of discrete items
        k (int): The chosen number of discrete items

    Raises:
        Exception: k cannot be negative

    Returns:
        int: _description_
    """
    if k > n:
        return 0
    if k < 0:
        raise Exception("Sorry, you cannot choose negative number of items")

    result = 1
    for i in range(1, min(k, n - k) + 1):
        result *= n
        result //= i
        n -= 1

    return result


def nChooseK(n: int, k: int) -> int:
    """formula for n choose k
       done in a recursion way

    Args:
        n (int): Total number of discrete items
        k (int): The chosen number of discrete items

    Raises:
        Exception: k cannot be negative

    Returns:
        int: _description_
    """
    if k == 0 or k == n:
        return 1
    if k > n:
        return 0
    if k < 0:
        raise Exception("Sorry, you cannot choose negative number of items")

    return nChooseK(n - 1, k - 1) + nChooseK(n - 1, k)
