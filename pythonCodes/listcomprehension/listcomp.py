# List comprehension create a list object
# which would consist of expression, iteration and condition
string = "Hello1234567"
number = [x for x in string if x.isdigit()]
mapped_number = map(int, number)
print(mapped_number)
