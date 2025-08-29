def compute_ratios(values):
    results = []
    for i in range(len(values)):
        for j in range(i, len(values)):
            try:
                denominator = values[j] - values[i]
                ratio = values[i] / denominator
            except ZeroDivisionError:
                ratio = None
            results.append((i, j, ratio))
    return results


nums = [5, 10, 15, 20, 25]
print(compute_ratios(nums))


