# Exercise 3 - Create new dictionary that counts letters from user provided string.
# I consulted chatGBT at https://chat.openai.com/ for this exercise and 
# the python cheat sheet provided on canvas at 
# https://github.com/akashp1712/awesome-python-cheatsheets/blob/master/Python_for_Java_developers_cheat_sheet.pdf

# Take user input
userInput = input('Enter a string: ');

# Letter count function
def letterCount(input):

    # Initialize new dictionary
    newDict = {}

    # Turn input into lowercase letters
    input = input.lower()

    # Loop over each character
    for i in input:
        if i != ' ' and i.isalpha(): # Determines occurances of letters in the string
            if i in newDict:
                newDict[i] += 1 # Counts when the letter is already in the new dictionary
            else:
                newDict[i] = 1 # Adds the letter to the new dictionary when the first occurance appears
    return newDict # Returns the new dictionary created

# Used to display the output
output = letterCount(userInput)
print(output)