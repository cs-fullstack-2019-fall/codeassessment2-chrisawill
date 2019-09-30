# ### Problem 6
# Create a class called ClubMember 
# Each club member has a name and a role  
# Create ClubMember instances for the following people:
# ```
# Alfred - Club President
# Troy - Club Vice President
# Albert - Club Secretary
# Bob - Club Treasurer
# ```
# Add each member instance to a new club_members list that you create.
# Write the code needed to loop through the club member list and print the current number of members in the list, then the member’s name and club role, one per line using f strings.

# Example Output:
# ```
# There are currently 4 club members in the list!

# Club President: Alfred
# Club Vice President: Troy
# Club Secretary: Albert
# Club Treasurer: Bob
# ```
class clubmewmber:
    def __init__(self, name, role):
        self.name = name
        self.role = role

member1 = clubmewmber("Alfred", "President")
member2 = clubmewmber("Troy", " Vice President")
member3 = clubmewmber("Albert", "Secratary")
member4 = clubmewmber("Bob", "Treasurer")

memarray = [member1, member2, member3, member4]
for eachmember in memarray:
    print(f"{memarray.index(0)} is {memarray.index(1)}")