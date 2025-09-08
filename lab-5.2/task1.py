import os
import bcrypt

# Load secret key from environment variable
SECRET_KEY = os.environ.get('SECRET_KEY')

# Simulated user database (username: hashed_password)
user_db = {
    'alice': bcrypt.hashpw(b'securepassword123', bcrypt.gensalt())
}

def register(username, password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    user_db[username] = hashed

def login(username, password):
    hashed = user_db.get(username)
    if not hashed:
        return False
    return bcrypt.checkpw(password.encode(), hashed)

# Example usage
if __name__ == "__main__":
    # Registration (never store plain passwords)
    username = input("Enter username to register: ")
    password = input("Enter password to register: ")
    register(username, password)
    print(f"User {username} registered.")

    # Login
    login_username = input("Enter username to login: ")
    login_password = input("Enter password to login: ")
    if login(login_username, login_password):
        print("Login successful!")
    else:
        print("Login failed.")