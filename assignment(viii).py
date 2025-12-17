class Player:
    player_count=0
    def __init__(self,name,level):
        self.name=name
        self.level=level
        Player.player_count +=1
    def numm_of_players(self):
        return f"number of players created {Player.player_count}"
        
p1=Player("rahul","l1")
print(p1.name,p1.level)
print(p1.numm_of_players())
p2=Player("rohan","l2")
print(p2.name,p2.level)
print(p2.numm_of_players())