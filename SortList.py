"""
written by : Muhammad Farooq Memon
Position: Student
Institute: Union College
"""
def find_middle(alist, target):
    """
    The following function finds a given number in a provided list
    :param alist: a list of all the numbers
    :param target: the number that is to be searched inside a list
    :return: True or False based on the presence of the target in the list
    """
    if len(alist) == 1:
        if target == alist[0]:
            #print(target)
            #print(alist[0])
            return True

        else:
            #print(target)
            #print(alist[0])
            return False

    if len(alist) == 0:
        #print(target)
        #print(alist[0])
        return False

    if len(alist) % 2 == 0:
        mid_pos = int(len(alist) / 2)
        #print(mid_pos, 'h')
        #print(alist)
        if target > alist[int(mid_pos)]:
            return find_middle(alist[mid_pos: len(alist)], target)
        if target == alist[int(mid_pos)]:
            return True
        else:
            return find_middle(alist[0: mid_pos], target)
    else:
        mid_pos = int((len(alist) + 1) / 2)
        #print(mid_pos, 'd')
        #print(alist)
        if target > alist[int(mid_pos)]:
            return find_middle(alist[mid_pos: len(alist)], target)
        if target == alist[int(mid_pos)]:
            return True
        else:
            return find_middle(alist[0: mid_pos], target)


if __name__ == "__main__":
    alist = [2, 4, 6, 7, 9, 10, 11, 12, 13, 13, 13, 14, 15]
    target = find_middle(alist, 14)
    print(target)
