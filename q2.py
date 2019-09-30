# ### Problem 2
# Prompt the user with the message, ‘Is it better to be rude or kind to People?’ 
# Keeping prompting the user to enter an answer until they enter the word kind. 
# Each time they enter something other than kind, print the message, ‘That’s not the answer I had hoped to hear. Try again.’ and prompt the user again.
# Once the user enters kind, print, ’Now that’s what I wanted to hear!’ and exit the program.



# ask the user for the kind promot
user = input("Is it better to be rude or kind to People?" )

#while loop here so it will never stop aking as long as the answer is wrong
while user != "kind":
    print("That’s not the answer I had hoped to hear. Try again.")
# aske here again to continiue the asking loop process
    user = input("Is it better to be rude or kind to People?" )
# no if else statement. else is fine by itself when there a while loop present
else:
    print("Now that’s what I wanted to hear!")