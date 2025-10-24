def bubble_sort(lst):
    """
    Sorts a list 'lst' in ascending order using the bubble sort algorithm.
    """
    n = len(lst)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                # Swap if the element found is greater than the next element
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

# Example test cases:
if __name__ == "__main__":
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
        [],
        [42],
        [3, 3, 2, 1, 2]
    ]
    for idx, arr in enumerate(test_cases):
        print(f"Original list #{idx+1}: {arr}")
        bubble_sort(arr)
        print(f"Sorted list #{idx+1}:   {arr}")
        print(f"Is sorted: {arr == sorted(arr)}\n")
