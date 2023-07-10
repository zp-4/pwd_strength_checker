import re
import string

def calculate_entropy(password):
    """
    Calculate the entropy of a password.
    """
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = lowercase.upper()
    numbers = "0123456789"
    special_chars = string.punctuation

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

    # Load wordlist of common weak passwords
    with open('weak_passwords.txt', 'r') as file:
        weak_passwords = {line.strip() for line in file}

    # Check if the password matches weak patterns
    if any(re.search(pattern, password, re.IGNORECASE) for pattern in weak_patterns):
        return True

    # Check if the password is a weak common password
    if password.lower() in weak_passwords:
        return True

    # Check if the password is all alphabets (either all lowercase or all uppercase)
    if password.isalpha():
        return True

    # Check if the password is all numeric
    if password.isnumeric():
        return True

    return False

def password_strength_checker(password):
    """
    Check the strength of a password and provide recommendations.
    """
    length = len(password)
    entropy = calculate_entropy(password)

    # Check if password is weak
    if is_weak_password(password):
        return "Weak password. Please choose a stronger password."

    # Check for moderate strength patterns
    if length >= 8 and length < 12:
        # Check for combinations of lower + number, lower + upper, lower + symbols, upper + number, upper + symbols
        if (any(char.islower() for char in password) and any(char.isdigit() for char in password)) or \
           (any(char.islower() for char in password) and any(char.isupper() for char in password)) or \
           (any(char.islower() for char in password) and any(char in string.punctuation for char in password)) or \
           (any(char.isupper() for char in password) and any(char.isdigit() for char in password)) or \
           (any(char.isupper() for char in password) and any(char in string.punctuation for char in password)):
            return "Moderate password. Consider increasing length and complexity for better security."

    # Check for strong password based on length and entropy
    if length >= 12 and entropy >= 60:
        return "Strong password. Well done!"

    # If none of the above conditions match, consider it a weak password
    return "Weak password. Please choose a stronger password."

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
