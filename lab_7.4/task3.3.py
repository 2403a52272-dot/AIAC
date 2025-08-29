try:
    # Open input.txt and output.txt safely
    with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
        for line in infile:
            outfile.write(line.upper())

    print("Processing done")

except FileNotFoundError:
    print("❌ Error: 'input.txt' not found. Please make sure the file exists in the same folder as this script.")
