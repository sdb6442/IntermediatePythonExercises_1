# Exercise 2 - New dict based off two dict inputs
# I consulted chatGBT at https://chat.openai.com/ for this exercise and 
# the python cheat sheet provided on canvas at 
# https://github.com/akashp1712/awesome-python-cheatsheets/blob/master/Python_for_Java_developers_cheat_sheet.pdf

# Dict function
def get_combined_dict(dict1, dict2): # Two dict parameters
    # Iterates through both dicts, determines if the letter appears in both dicts
    # returns the sum of the two ints associated with the strs when they appear in both dicts
    return {i: dict1[i] + dict2[i] for i in dict1 if i in dict2}


# Test code provided from Canvas
my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)