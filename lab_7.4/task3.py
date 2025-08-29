with open("example.txt", "w", encoding="utf-8") as f:
    user_input = input("Enter text to write to the file: ")
    f.write(user_input)