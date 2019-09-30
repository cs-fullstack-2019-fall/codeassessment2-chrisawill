# ### Problem 1
# Ask the user to enter a number. 
# Using the provided list of numbers, use a for loop to iterate the array and print out all the values that are smaller than the user input and print out all the values that are larger than the number entered by the user.

# ```
# # Start with this List
# list_of_many_numbers = [12, 24, 1, 34, 10, 2, 7]
# ```
# Example Input/Output if the user enters the number 9:
# ```
# The User entered 9
# 1  2  7 are smaller than 9
# 12  24  34  10 are larger than 97

# ```
# ask user for their number
user = int(input("Enter a number"))
list_of_many_numbers = [12, 24, 1, 34, 10, 2, 7]
# loop so that the user can check against everynumber
for eachnum in list_of_many_numbers:
    # conditionals. it prints out every number, the only flaw
    if user >= eachnum:
        lower = eachnum
        print(f"{user} is higher than{lower}")
    if user <= eachnum:
        higher = eachnum
        print(f"{user} is lower than{higher}")
