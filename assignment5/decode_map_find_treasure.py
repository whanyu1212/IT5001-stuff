def decode_map(mapfile, ddict, outfile):
    with open(mapfile, "r") as file1:
        rows = file1.readlines()
        for i in range(len(rows)):
            str = rows[i].strip("\n")
            for j in range(len(str)):
                if str[j] in ddict.keys():
                    rows[i] = rows[i].replace(str[j], ddict[str[j]])
    with open(outfile, "w") as file2:
        file2.writelines(rows)


def find_treasure(mapfile):
    with open(mapfile, "r") as map:
        row_counter = 0
        map_rows = map.readlines()
        for i in range(len(map_rows)):
            str = map_rows[i]
            for j in range(len(str)):
                if str[j] == "T":
                    return (row_counter + 1, j)
            row_counter += 1
    return None
