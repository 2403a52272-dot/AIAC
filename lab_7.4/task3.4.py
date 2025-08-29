squares = []
# Read numbers safely
with open("numbers.txt", "r") as f:
    nums = f.readlines()

for n in nums:
    n = n.strip()
    if n.lstrip('-').isdigit():
        squares.append(int(n) ** 2)

# Write squares safely
with open("squares.txt", "w") as f2:
    for sq in squares:
        f2.write(str(sq) + "\n")

print("Squares written")