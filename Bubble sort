def swap_data(n, list_):
    swaped = False
    # Go up to n-1 because you compare list_[i] and list_[i + 1]
    for i in range(n - 1): 
        if list_[i] > list_[i + 1]:
            # swap the elements
            list_[i], list_[i + 1] = list_[i + 1], list_[i]
            swaped = True
    return swaped

def bubble_sort(list_data):
    """
    Bubble Sort implementation
    """
    for i in range(len(list_data)-1, 0, -1):  # Loop backwards
        # Call swap_data and check if any swaps were made
        swaped = swap_data(i, list_data)
        
        # If no swap was made, the list is already sorted
        if not swaped:
            break

    return list_data
