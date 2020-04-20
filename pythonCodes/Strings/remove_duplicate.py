# Program to remove duplicate characters within a string

def remove_duplicatechars(str_var):
    s = set()
    list = []
    for ch in str_var:
        if ch not in s:
            s.add(ch)
            list.append(ch)

    return ''.join(list)

print(remove_duplicatechars("Geeks for Geeks"))
