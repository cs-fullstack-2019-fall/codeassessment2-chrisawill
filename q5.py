# ### Problem 5
# Create a SportsTeam Class for tracking sports teams. The class should have the properties team_name_p, team_city, and team_ranking_p.
# The class should have a method to change a Team’s ranking. 
# The class should implement the ```__str__``` method so that when an instance of the SportsTeam is printed it will output a string containing the team name, team city, and team rank (use f strings to format the output).
# Your program should create a SportsTeam instance with an initial ranking of 2.
# Print out the class.
# Your program should change the ranking of the team to 8 using only the class method.
# Print out the class (should use your ```__str__``` method).


# Example Output:
# ```
# The Grizzlies are from Memphis and are 2 in the standings.
# # Update the rating from 2 to 8 from your code
# The Grizzlies are from Memphis and are 8 in the standings.
# ```

# make your sport class
class Sportsteam:
    def __init__(self, name, city, ranking):
        self.name = name
        self.city = city
        self.ranking = ranking
# both functions to change ranking and format in f string
    def changeR(self):
        self.ranking = newrank
    def myteam(self):
        print(f"{self.name} will be in {self.city} in {self.ranking} place.")

# instance of my team. print funtion isnt working
newteam = Sportsteam("bears", "toronto", 2)
newrank = 8
