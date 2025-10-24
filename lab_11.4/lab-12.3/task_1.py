
def linear_search(lst, value):
    """
    Performs linear search for 'value' in 'lst'.
    Returns the index if found, else returns -1.
    """
    for idx, elem in enumerate(lst):

        if elem == value:
            return idx
    return -1
# test cases:
print(linear_search([1, 2, 3, 4, 5], 3)) # should return 2
print(linear_search([1, 2, 3, 4, 5], 6)) # should return -1
print(linear_search([1, 2, 3, 4, 5], 1)) # should return 0
print(linear_search([1, 2, 3, 4, 5], 5)) # should return 4
print(linear_search([1, 2, 3, 4, 5], 0)) # should return -1
print(linear_search([1, 2, 3, 4, 5], 6)) # should return -1
print(linear_search([1, 2, 3, 4, 5], 1)) # should return 0
print(linear_search([1, 2, 3, 4, 5], 5)) # should return 4
print(linear_search([1, 2, 3, 4, 5], 0)) # should return -1
print(linear_search([1, 2, 3, 4, 5], 6)) # should return -1
print(linear_search([1, 2, 3, 4, 5], 1)) # should return 0
print(linear_search([1, 2, 3, 4, 5], 5)) # should return 4
print(linear_search([1, 2, 3, 4, 5], 0)) # should return -1