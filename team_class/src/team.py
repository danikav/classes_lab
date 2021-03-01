class Team:
    def __init__(self, name, players, coach, points=0):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = points
    
    def change_coach(self,coach):
        self.coach = coach
    
    def add_player(self, player):
        self.players.append(player)

    def has_player(self, player):
        if player in self.players:
            return True
        else:
            return False

    def play_game(self, win):
        if win == True:
            self.points += 3
        
    

    