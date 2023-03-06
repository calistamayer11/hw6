# TODO: implement the 4 functions (as always, include docstrings & comments)


def find_zero(L):
    """Return the index of the 0 in a half-sorted list in O(log(n))"""
    left, right = 0, len(L) - 1
    while left <= right:
        mid = (left + right) // 2
        if L[mid] == 0:
            return mid
        elif L[mid] < 0:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def bubble(L, left, right):
    """Sort the sub-list L[left:right] using bubble sort"""
    for i in range(right - 1, left - 1, -1):
        for j in range(left, i):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]


def selection(L, left, right):
    pass


def insertion(L, left, right):
    pass


def sort_halfsorted(L, sort):
    """Efficiently sorts a list comprising a series of negative items, a single 0, and a series of positive items

    Input
    -----
        * L:list
            a half sorted list, e.g. [-2, -1, -3, 0, 4, 3, 7, 9, 14]
                                     <---neg--->     <----pos----->

        * sort: func(L:list, left:int, right:int)
            a function that sorts the sublist L[left:right] in-place
            note that we use python convention here: L[left:right] includes left but not right

    Output
    ------
        * None
            this algorithm sorts `L` in-place, so it does not need a return statement

    Examples
    --------
        >>> L = [-1, -2, -3, 0, 3, 2, 1]
        >>> sort_halfsorted(L, bubble)
        >>> print(L)
        [-3, -2, -1, 0, 1, 2, 3]
    """

    idx_zero = find_zero(L)  # find the 0 index
    sort(L, 0, idx_zero)  # sort left half
    sort(L, idx_zero + 1, len(L))  # sort right half
