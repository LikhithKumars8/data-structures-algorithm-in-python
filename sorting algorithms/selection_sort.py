def selection_sort(data):
    """
    Sorts a list in ascending order using the Selection Sort algorithm.

    Selection Sort works by repeatedly finding the smallest element in 
    the unsorted portion of the list and swapping it with the first 
    element of the unsorted portion. This process continues until the 
    entire list is sorted.

    Parameters:
        data (list): A list of elements to be sorted.
        
    Returns:
        list: The sorted list.
    """
    
    # Get the length of the list
    n = len(data)
    
    # Iterate through the entire list
    for i in range(n - 1):
        # Assume the current index is the smallest
        min_index = i
        
        # Find the smallest element in the unsorted portion of the list
        for j in range(i + 1, n):
            if data[j] < data[min_index]:
                min_index = j  # Update the index of the smallest element
        
        # Swap the found smallest element with the first element of the unsorted portion
        data[i], data[min_index] = data[min_index], data[i]
        
        # Debugging statement to see the list after each swap (optional)
        print(f"After pass {i + 1}: {data}")
    
    return data  # Return the sorted list

# Example usage:
data = [64, 2, 3, 5, 6, 11]
print("Original list:", data)
sorted_data = selection_sort(data)
print("Sorted list:", sorted_data)
