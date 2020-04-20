# String program to find the digitas within a string
def check_digit_in_str(str_var):
    digits = []
    for i in str_var:
        if i.isdigit():
            digits.append(i)

    for i in digits:
        print(i)

    print("Total number of digits in the string is: "+str(len(digits)))

check_digit_in_str("H311o")
