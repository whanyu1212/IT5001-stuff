parent = {
    "Amy": "Ben",
    "May": "Tom",
    "Tom": "Ben",
    "Ben": "Howard",
    "Howard": "George",
    "Frank": "Amy",
    "Joe": "Bill",
    "Bill": "Mary",
    "Mary": "Philip",
    "Simon": "Bill",
    "Zoe": "Mary",
}


def is_ancestor(name1: str, name2: str, parent: dict) -> bool:
    """Based on the parent dictionary, check if name1 is an ancestor of name2

    Args:
        name1 (str): name in string
        name2 (str): name in string
        parent (dict): reference dictionary

    Returns:
        bool: True or False
    """
    generation_list = []
    current_gen = name2
    while current_gen in parent.keys():
        generation_list.append(parent[current_gen])
        if parent[current_gen] in parent.keys():
            current_gen = parent[current_gen]
        else:
            break
    if name1 in generation_list:
        return True
    else:
        return False


# helper function
def find_all_ancestors(name: str, parent: dict) -> list:
    """Find all the ancestors of a given name

    Args:
        name (str): input name
        parent (dict): reference dictionary

    Returns:
        list: list of ancestors or people who are generations before him/her
    """
    ancestor_list = []
    current_gen = name
    while current_gen in parent.keys():
        ancestor_list.append(parent[current_gen])
        if parent[current_gen] in parent.keys():
            current_gen = parent[current_gen]
        else:
            break
    return ancestor_list


def is_related(name1: str, name2: str, parent: dict) -> bool:
    """Validate if two names are related by
     checking if they have a common ancestors in
     the list or are they ancestors of each other

    Args:
        name1 (str): person 1
        name2 (str): person 2
        parent (dict): reference dictionary

    Returns:
        bool: True or False
    """
    intersection = []
    name1_ancestors = find_all_ancestors(name1, parent)
    name2_ancestors = find_all_ancestors(name2, parent)

    for name in name1_ancestors:
        if name in name2_ancestors:
            intersection.append(name)
    print(intersection)
    if len(intersection) >= 1:
        return True
    elif is_ancestor(name1, name2, parent) or is_ancestor(name2, name1, parent):
        return True
    else:
        return False


print("Is Mary an ancestor of Simon?")
print(is_ancestor("Mary", "Simon", parent))
print("Is Zoe an ancestor of Joe?")
print(is_ancestor("Zoe", "Joe", parent))
print()

"""
print("Is Joe is_related to Philip?")
print(is_related('Joe','Philip',parent))
print("Is Amy is_related to May?")
print(is_related('Amy','May',parent))
print("Is Amy is_related to Philip?")
print(is_related('Amy','Philip',parent))    
print()


parent['Ben']='Philip' #modify the dictionary so that Philip is Ben's parent
print("After Philip became Ben\'s parent...")
print("Is Amy is_related to Philip?")
print(is_related('Amy','Philip',parent))
"""
