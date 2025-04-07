def reverse_string(s):
    return s[::-1]
def is_palindrome(s):
    return s==reverse_string(s)

string=input("Enter a string:")

reversed_string=reverse_string(string)
print("Reversed string:",reversed_string)

if is_palindrome(string):
    print("The given string is palindrome")
else:
    print("The given string is not a palindrome")

    
