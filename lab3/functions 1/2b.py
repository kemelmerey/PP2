#Write a Python function that takes a list and returns a new list with unique elements of the first list. 
#Note: don't use collection set.
def unique_list(list):
    unique_list = []
    for element in list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list
# Example
list = [1, 2, 2, 3, 3, 5]
print(unique_list(list))
#output:[1, 2, 3, 5]
