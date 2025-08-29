def sort_by_type(data):
    """Sorts a list by data type first (integers before strings), then by value."""
    return sorted(data, key=lambda x: (isinstance(x, str), x))

items = [3, "apple", 1, "banana", 2]
print(sort_by_type(items))