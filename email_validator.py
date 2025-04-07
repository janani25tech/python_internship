import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))


email = input("Enter an email: ")
print("Valid Email" if is_valid_email(email) else "Invalid Email")
