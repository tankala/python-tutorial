grocery_list = ["Rice", "Cooking Oil", "Paste", "Bath Soap", "Detergent Powder", "Shampoo"]

# To add any item at last
grocery_list.append("Face Cream")
print(grocery_list)

# To insert item at a prticular index
grocery_list.insert(2, "Coconut Oil")
print(grocery_list)

# To find item index
if "Olive Oil" in grocery_list:
    print(grocery_list.index("Olive Oil"))
print(grocery_list.index("Cooking Oil"))

# To know element count
grocery_list.append("Paste")
print(grocery_list)
print(grocery_list.count("Olive Oil"))
print(grocery_list.count("Paste"))

# List Copy
grocery_list_copy = grocery_list.copy()
grocery_list.append("Paracetamol")
print(grocery_list)
print(grocery_list_copy)

# To merge 2 lists
sub_grocery_list = ["Atta", "Floor"]
grocery_list.extend(sub_grocery_list)
print(grocery_list)

# To reverse items in list
print(grocery_list)
grocery_list.reverse()
print(grocery_list)

# For sorting list items in ascending order
print(grocery_list)
grocery_list.sort()
print(grocery_list)
# For Descending order
grocery_list.reverse()
print(grocery_list)

# To remove an item
print(grocery_list)
grocery_list.remove("Paste")
print(grocery_list)

# To remove last item
print(grocery_list)
grocery_list.pop()
print(grocery_list)

# To clear list
grocery_list.clear()
print(grocery_list)