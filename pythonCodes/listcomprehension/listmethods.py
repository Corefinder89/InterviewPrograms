list = ["Movies", "Music", "Pictures"]

# Append list
list.append("Files")
print("Append: {}".format(list))

#Insert into list
list.insert(2, "Documents")
print("Insert: {}".format(list))

#Remove from list
list.remove("Pictures")
print("Remove: {}".format(list))

#Extend will join two lists
list2=["Music2", "Movies2"]
list.extend(list2)
print("Extend: {}".format(list))
