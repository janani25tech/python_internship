import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    special_char_error = re.search(r"[@_!#$%^&*()<>?/\\|}{~:]", password) is None

    if length_error or digit_error or uppercase_error or lowercase_error or special_char_error:
        print("Weak password. Issues found:")
        if length_error:
            print("- Minimum length should be 8 characters")
        if digit_error:
            print("- Include at least one digit")
        if uppercase_error:
            print("- Include at least one uppercase letter")
        if lowercase_error:
            print("- Include at least one lowercase letter")
        if special_char_error:
            print("- Include at least one special character")
    else:
        print("Strong password!")

# Example usage
password_input = input("Enter your password: ")
check_password_strength(password_input)
