from hashlib import sha256

def hash_password(password: str) -> str:
    return sha256(password.encode()).hexdigest()

def login(email: str, password_to_check: str, stored_logins: dict) -> bool:
    if email not in stored_logins:
        return False  # Email not found

    hashed_input = hash_password(password_to_check)
    return stored_logins[email] == hashed_input

def main():
    # Sample stored logins (Email -> Hashed Password)
    stored_logins = {
        "user@example.com": hash_password("securepassword"),
        "admin@website.com": hash_password("admin123"),
        "test@demo.com": hash_password("testpass")
    }

    print("Welcome to Secure Login System")

    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if login(email, password, stored_logins):
        print("Login successful! ✅")
    else:
        print("Invalid email or password. ❌")

if __name__ == '__main__':
    main()
