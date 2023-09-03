# Unique Elements
# I consulted chatGBT to complete this exercise

# Created function with a list as a parameter
def unique_Elements(original_List):
    new_Unique_List = []
    for i in original_List:  # Loops through given list
        if i not in new_Unique_List: # If an integer is not present in the new unique list, it is added to the new list.
            new_Unique_List.append(i)
    return new_Unique_List # Returns new list with unique integers

# Test list
my_list = [1, 2, 3, 4, 18, 9, 1, 3, 99, 18, 24]

# Create new list by running function on the Test List
unique_List = unique_Elements(my_list)

# Print List
print(unique_List)
