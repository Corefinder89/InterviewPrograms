# String program to find the duplicate characters within a string
def find_duplicates(str_var):
    duplicates = []
    for i in str_var:
        if str_var.count(i) > 1:
            if i not in duplicates:
                duplicates.append(i)
    print(*duplicates)

find_duplicates("tutorialspoint")
