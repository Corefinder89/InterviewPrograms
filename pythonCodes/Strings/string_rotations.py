# Check if one string is a rotation of other
def are_rotations(str_var1, str_var2):
    str_len1 = len(str_var1)
    str_len2 = len(str_var2)
    temp = ''

    if str_len1 != str_len2:
        return 0

    temp = str_var1+str_var2

    if(temp.count(str_var2) > 0):
        return 1
    else:
        return 0

if are_rotations('ABACD', 'CDABA'):
    print("Strings are rotations of each other")
else:
    print("Strings are not rotations of each other")
