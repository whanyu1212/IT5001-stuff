def decipher_message(msg: str, guide: dict) -> str:
    """decipher a string based on the reference in dict

    Args:
        msg (str): input string
        guide (dict): reference dictionary

    Returns:
        str: translated string
    """
    result = ""
    for char in msg:
        if char in guide.keys():
            result += guide[char]
        else:
            result += char
    return result
