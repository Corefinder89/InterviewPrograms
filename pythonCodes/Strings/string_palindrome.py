# Check if a given string is palindrome
def is_palindrome(str_var):
    str_var = str_var.lower()
    rev_str_var = str_var[::-1]

    if str_var == rev_str_var:
        print("String is palindrome")
    else:
        print("String is not palindrome")

is_palindrome("Mam")
