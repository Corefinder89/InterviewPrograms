# Given a string how to find the longest palindromic substring within a string
def longest_palindromic_substring(str_var):
    str_var = str_var.lower()
    pal_string = []
    longest_pal_string = ''
    split_val = str_var.split(' ')
    for i in split_val:
        rev_i = i[::-1]
        if i == rev_i:
            pal_string.append(i)

    # max_len = -1
    # for i in pal_string:
    #     if len(i) > max_len:
    #         max_len = len(i)
    #         longest_pal_string = i

    longest_pal_string = max(pal_string, key=len)

    print(longest_pal_string)

longest_palindromic_substring("My mom who is my favourite mum and mam is rowing in kayak")
