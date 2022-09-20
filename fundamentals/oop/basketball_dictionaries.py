#Challenge 1: Update the Constructor
class Player:

    def __init__(self,data):
        self.name = data["name"]
        self.age = data["age"]
        self.position = data["position"]
        self.team = data["team"]

    # Ninja Bonus  Add an @class method called get_team(cls, team_list) that, given a list of dictionaries populates and returns a new list of Player objects.

    @classmethod
    def get_team(cls,team_list):
        # team_list=Player(cls)
        # new_team.append(team_list)
        print(team_list)
        return team_list
    

kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
}
    
#2Create instances using individual player dictionaries
player_kevin=Player(kevin)
player_jason=Player(jason)
player_kyrie=Player(kyrie)
print(player_jason.name,player_jason.age)

# 3 Make a list of Player instances from a list of dictionaries
# ... (class definition and large list of players here)
players = [
    {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
    },
    {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Damian Lillard", 
    "age":33, "position": "Point Guard", 
    "team": "Portland Trailblazers"
    },
    {
    "name": "Joel Embiid", 
    "age":32, "position": "Power Foward", 
    "team": "Philidelphia 76ers"
    },
    {
    "name": "", 
    "age":16, 
    "position": "P", 
    "team": "en"
    }
]
new_team=[]
# el can be called any variable as it will be replaced by data in init method
for el in players: 
    #call __init__ function here
    player=Player(el)
    new_team.append(player)
    print(player.age,player.name,player.position,player.team)

Player.get_team(new_team)

