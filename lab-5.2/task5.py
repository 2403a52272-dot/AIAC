def greet_user(name, gender):
    """Greets a user with a title based on their gender, with a gender-neutral option."""
    # Using a dictionary for a cleaner way to map genders to titles
    titles = {
        "male": "Mr.",
        "female": "Ms.",
        "non-binary": "Mx."  # Mx. is a common gender-neutral title
    }
    
    # Get the title from the dictionary, defaulting to a gender-neutral option if not found
    title = titles.get(gender.lower(), "Hello,")
    
    # The greeting format changes slightly if a specific title is used
    if title in ["Mr.", "Ms.", "Mx."]:
        return f"Hello, {title} {name}! Welcome."
    else:
        return f"Hello, {name}! Welcome."

# Example usage to demonstrate the new functionality
print(greet_user("Alex", "non-binary"))
print(greet_user("Jane", "female"))
print(greet_user("John", "male"))
print(greet_user("Casey", "prefer not to say"))