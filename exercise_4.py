# Exercise 4 - Add 5 inputs together
# I learned how to determine if an input is an int by using a try/catch statement from the following link
# found on StackOverFlow https://stackoverflow.com/questions/8075877/converting-string-to-int-using-try-except-in-python
# The rest of my code I learned from completing the intro exercises in the previous
# module that focused on lists.

# Determines if input is an integer.
# Returns the input if it is an integer and returns a statement if it isn't.
def intTest(num):
    while True:
        try:
            # Tests if the input is an integer.
            return int(input(num))
        except ValueError:
            # If input is not an integer, an error message is printed.
            print("Invalid input. Please enter an int.")

# Initialize an empty list to add input
list1 = []
for i in range (1, 6, +1):
    # Prompts input and tests input
    inputResult = intTest('Enter int #' + str(i) + ': ');
    # Adds the input to the list when it passes the intTest, meaning the input is an integer.
    list1.append(inputResult)

# Calculates the sum of the list
Sum = sum(list1)

# Prints the sum
print('Your sum is ' + str(Sum))