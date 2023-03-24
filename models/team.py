class Team:
    def __init__(self, name, attack, defence, matches_played, wins, id=None):
        self.name = name
        self.attack = attack
        self.defence = defence
        self.matches_played = matches_played
        self.wins = wins
        self.id = id

    #  increment matches played
    def update(self, result):
        self.matches_played += 1
        if result:
            self.wins += 1

    #  train and improve skill ratings
