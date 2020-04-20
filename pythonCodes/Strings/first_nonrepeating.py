# Print the first non repeated charcter within a string
def first_nonrepeating(str_var):
    nr = [char for char in str_var if str_var.count(char)==1]
    print(nr[0])

first_nonrepeating("GeeksforGeeks")
