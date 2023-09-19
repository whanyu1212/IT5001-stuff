d1 = {
    "D": "W",
    "1": "W",
    "Z": "W",
    "C": "T",
    "3": "T",
    "F": "T",
    "0": ".",
    "2": ".",
    "4": ".",
    "B": "^",
    "+": "^",
    ";": "^",
    "Q": "E",
    "7": "E",
    "8": "E",
    "X": "M",
    "P": "M",
    "!": "M",
    "(": ":",
    ")": ":",
    "9": ":",
    "*": " ",
    "|": " ",
    "#": " ",
}
d2 = {
    "C": "W",
    "3": "W",
    "F": "W",
    "0": "T",
    "2": "T",
    "4": "T",
    "B": ".",
    "+": ".",
    ";": ".",
    "Q": "^",
    "7": "^",
    "8": "^",
    "D": "E",
    "1": "E",
    "Z": "E",
    "(": "M",
    ")": "M",
    "9": "M",
    "*": ":",
    "|": ":",
    "#": ":",
    "X": " ",
    "P": " ",
    "!": " ",
}


def decode_map(mapfile: str, ddict: dict, outfile: str) -> None:
    """open the encoded mapfile, decode the map,
    based on referene dctionary and write the
    decoded map to outfile

    Args:
        mapfile (str): input map file directory
        ddict (dict): reference dictionary
        outfile (str): decoded map file directory
    """
    with open(mapfile, "r") as file1, open(outfile, "w") as file2:
        for line in file1:
            decoded_line = ""
            for char in line.strip("\n"):
                if char in ddict:
                    decoded_line += ddict[char]
                else:
                    decoded_line += char
            decoded_line += "\n"
            file2.write(decoded_line)


from typing import Union, Tuple


def find_treasure(mapfile: str) -> Union[Tuple[int, int], None]:
    """Open the decoded mapfile,
    find the treasure and return the
    location of the treasure based on
    the string pattern in the area

    Args:
        mapfile (str): input file directory

    Returns:
        Union[Tuple[int, int], None]: return (i,j) of the treasure location or None if not found
    """
    with open(mapfile, "r") as map:
        map_rows = map.readlines()
        for i in range(len(map_rows)):
            for j in range(len(map_rows[i])):
                if (
                    map_rows[i][j] == "T"
                    and map_rows[i + 1][j - 1] == "T"
                    and map_rows[i + 1][j] == "T"
                    and map_rows[i + 1][j + 1] == "T"
                    and map_rows[i + 2][j] == "T"
                ):
                    return (i + 1, j)
    return None


# print("Map 1")
# decode_map("encoded_map.txt", d1, "decoded_map.txt")
# print(find_treasure("decoded_map.txt"))

# Uncomment the following for your test cases
"""
print("Map 2")
decode_map('encoded_map2.txt',d1,'decoded_map2.txt')
print(find_treasure('decoded_map2.txt'))

print("Map 3")
decode_map('encoded_map3.txt',d1,'decoded_map3.txt')
print(find_treasure('decoded_map3.txt'))

print("Map 5")
decode_map('encoded_map5.txt',d1,'decoded_map5.txt')
print(find_treasure('decoded_map5.txt'))

print("Map 1 B")
decode_map('encoded_mapB.txt',d2,'decoded_mapB.txt')
print(find_treasure('decoded_mapB.txt'))
"""
