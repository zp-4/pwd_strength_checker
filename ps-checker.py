import re

def calculate_entropy(password):
    """
    Calculate the entropy of a password.
    """
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = lowercase.upper()
    numbers = "0123456789"
    special_chars = r"!@#\$%\^&\*\(\)_\+=-\{\}\[\]\|\\:;\"'<>,\.\?/"

    charsets = [lowercase, uppercase, numbers, special_chars]
    entropy = sum(len(charset) for charset in charsets if any(char in password for char in charset))

    entropy *= len(password)

    return entropy

def is_weak_password(password):
    """
    Check if the password is weak based on common patterns and known weak passwords.
    """
    weak_patterns = [
        r"\bpassword\b",
        r"\b123456\b",
        r"\bqwerty\b",
        # Add more weak patterns as needed
    ]

    return any(re.search(pattern, password, re.IGNORECASE) for pattern in weak_patterns)

def password_strength_checker(password):
    """
    Check the strength of a password and provide recommendations.
    """
    length = len(password)
    entropy = calculate_entropy(password)

    if length < 8 or entropy < 40 or is_weak_password(password):
        return "Weak password. Please choose a stronger password."
    elif length < 12 or entropy < 60:
        return "Moderate password. Consider increasing length and complexity."
    else:
        return "Strong password. Well done!"

def get_user_password():
    """
    Prompt the user to enter a password securely.
    """
    import getpass
    password = getpass.getpass("Enter your password: ")
    return password

def main():
    """
    Main function to execute the password strength checking.
    """
    password = get_user_password()
    strength = password_strength_checker(password)
    print(strength)

if __name__ == "__main__":
    main()
