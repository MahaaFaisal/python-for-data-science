

def count_in_list(lst, item):
    """ a function that counts how many of the item in the list

    lst -- the list to count items in
    item -- the item to be counted
    """
    count = 0
    for i in lst:
        if (i == item):
            count = count + 1
    return count
