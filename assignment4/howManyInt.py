from typing import Union


def howManyInt(l: Union[tuple, list]) -> int:
    """Start with a counter of 0, loop through the collection,
    and count the number of integers in the collection

    Args:
        l (Union[tuple, list]): either a list or a tuple

    Returns:
        int: integer count
    """
    count = 0
    for element in l:
        if type(element) == int:
            count += 1
    return count


# test case 1
if __name__ == "__main__":
    count = howManyInt([1, 2, 2.3, 3, 10.0, [2, 3, 4], "ab", 3, "1"])
    print(count)
