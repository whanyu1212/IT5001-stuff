from typing import Union


# def matchResistors(R: Union[tuple, list], n: int) -> list:
#     """This question is a variation of the two sum problem.
#     create a dictionary to store the frequency of every possible
#     difference between n and the elements in R. Loop through R,
#     and check if the difference between n and the current element.
#     If the difference is in the dictionary and the frequency is more than 0,
#     add the pair to the output list. Otherwise, add the current difference value
#     to the dictionary.
#     Once a pair is matched, -1 from the counter which is the value of the dictionary
#     so this takes care of duplicates
#     Args:
#         R (Union[tuple, list]): input collection of values
#         n (int): target number that a pair needs to sum up to

#     Returns:
#         list: a list of tuples
#     """
#     num_freq = {}  # {difference: freq}
#     pairs = []  # output list

#     for num in R:
#         diff = n - num  # calculate the difference

#         if diff in num_freq and num_freq[diff] > 0:
#             pair = (num, diff)
#             pairs.append(tuple(sorted(pair)))
#             num_freq[diff] -= 1
#         else:
#             num_freq[num] = num_freq.get(num, 0) + 1

#     return pairs


def matchResistors(R: Union[tuple, list], n: int) -> list:
    R.sort()
    left, right = 0, len(R) - 1

    pairs = []  # Output list to store pairs

    while left < right:
        current_sum = R[left] + R[right]

        if current_sum == n:
            pairs.append((R[left], R[right]))
            left += 1
            right -= 1
        elif current_sum < n:
            left += 1
        else:
            right -= 1

    return pairs


if __name__ == "___main__":
    output = matchResistors([2, 7, 11, 15], 9)
    print(output)
