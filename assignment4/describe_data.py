def describe_data(L: list | tuple) -> None:
    """Describe the data type of each element in the
    collection. The collection can either be a list
    or a tuple.

    Args:
        input (list | tuple): input collection
    """
    # for element in L:
    #     print(f"The type of the element {element} is {type(element)}")
    for element in L:
        print("The type of the element", element, "is", type(element))


if __name__ == "__main__":
    # test case 1
    describe_data([3.1415, True, 42, "88", (1, 2), [1, [2]]])
