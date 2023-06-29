#!/usr/bin/python3
""" 
pascal triangle
"""
def pascal_triangle(n):
    """ 
    returns pascal triangle
    """
    if n <= 0:
        return []

    pTran = []

    for i in range(n):
        # firs
        my_List = [1]
        if i == 0:
            pTran.append(my_List)
            continue

        k = i - 1
        for j in range(len(pTran[k])):
            if j + 1 == len(pTran[k]):
                # last element
                my_List.append(1)
                break
            # Add two previous values to get current next value
            nextVal = pTran[k][j] + pTran[k][j + 1]
            my_List.append(nextVal)
        pTran.append(my_List)

    return pTran
