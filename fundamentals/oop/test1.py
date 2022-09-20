class Player:
    def __init__(self,data): 
        self.name = data[0]
        self.age = data[1]
        self.position = data[2]
        self.team = data[3]
    
    # def __init__(self, name, age, position, team):
    #     self.name = name
    #     self.age = age
    #     self.position = position
    #     self.team = team

kevin = {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"}

jason=["Jason",34,"small forward","Brooklyn Nets"]

# Create instance of class
# player_kevin = Player(kevin)
# print(player_kevin.name,player_kevin.age)

player_jason=Player(jason)
print(player_jason.name,player_jason.age)

