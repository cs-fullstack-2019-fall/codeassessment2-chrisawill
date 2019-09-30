# ### Problem 4
# Write a program that allows users to compare words by their length. Implement a function called chk_strings that accepts 2 strings entered by the user and compares them by length
# The function should return true if the first string parameter has more characters (i.e. longer) than the second string passed into the function, otherwise, the function should return false.
# DO NOT print the result in the function, print the result using the return value provided by the function. 

# Example Input/Output:
# ```
# Enter the first string: BIRD
# Enter the second string: COW

# BIRD is longer than COW
# ```

user1 = input("Enter a word. ")
user2 = input("enter another word.")

def answer1():
    print(f"{user1} is longer than {user2}")
def answer2():
    print(f"{user1} is not longer than {user2}")

def chk_strings():
    if len(user1) == len(user2):
        return answer1
    elif len(user1) != len(user2):
        return answer2
