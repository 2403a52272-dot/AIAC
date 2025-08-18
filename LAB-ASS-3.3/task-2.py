def bubble_sort(arr):
    """
    Sorts a list of numbers in ascending order using the bubble sort algorithm.

    Args:
        arr (list): List of numbers to sort.

    Returns:
        list: New sorted list in ascending order.

    Example:
        >>> bubble_sort([5, 2, 9, 1])
        [1, 2, 5, 9]
        >>> bubble_sort([])
        []
        >>> bubble_sort([3])
        [3]
    """
    n = len(arr)
    result = arr.copy()
    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result

# Example input/output demonstration
if __name__ == "__main__":
    test_cases = [
        [5, 2, 9, 1],
        [],
        [3],
        [4, 4, 2, 2],
        [10, 9, 8, 7]
    ]
    print("Bubble Sort Example Input/Output:")
    for arr in test_cases:
        print(f"Input: {arr} -> Output: {bubble_sort(arr)}")
