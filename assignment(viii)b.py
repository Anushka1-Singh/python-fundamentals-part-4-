class Player:
    player_count = 0  # Class variable: keeps track of total players created (shared by all instances)

    def __init__(self, name, level):
        self.name = name       # Instance variable: stores the name of this specific player
        self.level = level     # Instance variable: stores the level of this specific player
        Player.player_count += 1  # Increment the class variable every time a new player is created

    @classmethod
    def total_players(cls):
        # Class method: returns the total number of players created
        # Uses 'cls' to access class-level variables instead of instance variables
        return f"Number of players created: {cls.player_count}"

# Create first player object
p1 = Player("Rahul", "L1")
print(p1.name, p1.level)         # Print instance data: name and level of p1
print(Player.total_players())    # Call class method to get total number of players

# Create second player object
p2 = Player("Rohan", "L2")
print(p2.name, p2.level)         # Print instance data: name and level of p2
print(Player.total_players())    # Call class method again to get updated total players