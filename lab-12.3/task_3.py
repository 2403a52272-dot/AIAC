from scipy.optimize import linprog

# Objective: Maximize profit = 6A + 5B
# linprog minimizes by default, so use negative coefficients
c = [-6, -5]

# Constraints:
# 1. Milk: 1*A + 1*B <= 5
# 2. Choco: 3*A + 2*B <= 12
A = [
    [1, 1],   # Milk constraint
    [3, 2]    # Chocolate constraint
]
b = [5, 12]

# Bounds: A >= 0, B >= 0
bounds = [(0, None), (0, None)]

# Solve using linprog
res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

if res.success:
    A_units = res.x[0]
    B_units = res.x[1]
    max_profit = 6 * A_units + 5 * B_units

    # Calculate resource usage
    milk_used = 1 * A_units + 1 * B_units
    choco_used = 3 * A_units + 2 * B_units

    print("=" * 50)
    print("CHOCOLATE MANUFACTURING OPTIMIZATION SOLUTION")
    print("=" * 50)
    print(f"Optimal number of units to produce:")
    print(f"  Chocolate A: {A_units:.2f} units")
    print(f"  Chocolate B: {B_units:.2f} units")
    print(f"\nMaximum Profit: Rs {max_profit:.2f}")
    print(f"\nResource Usage:")
    print(f"  Milk used: {milk_used:.2f} units (available: 5)")
    print(f"  Choco used: {choco_used:.2f} units (available: 12)")
    print(f"\nConstraints satisfied:")
    print(f"  Milk constraint: {milk_used:.2f} <= 5 {'[OK]' if milk_used <= 5 else '[VIOLATED]'}")
    print(f"  Choco constraint: {choco_used:.2f} <= 12 {'[OK]' if choco_used <= 12 else '[VIOLATED]'}")
else:
    print("Optimization failed:", res.message)
