import random

from utils.generate_player import generate_player

class Team:
    def __init__(self, name, attack, defence, matches_played, wins, cup_wins=0, bank_balance=5000, id=None):
        self.name = name
        self.attack = attack
        self.defence = defence
        self.matches_played = matches_played
        self.wins = wins
        self.cup_wins = cup_wins
        self.id = id
        self.bank_balance = bank_balance
        self.players = []

    #  increment matches played
    def update(self, result):
        self.matches_played += 1
        if result:
            self.wins += 1

    def generate_players(self, team_type):
        
        for i in range(10):
            player = generate_player(self.name, self.id, team_type, i)
            self.players.append(player)
        self.set_skill_levels()   

        return self.players


    def set_skill_levels(self):
        for player in self.players:
            if player.position == "Attack":
                self.attack += player.skill_level
            if player.position == "Defence":
                self.defence += player.skill_level

        self.attack = round(self.attack/4)
        self.defence = round(self.defence/6)

    def select_scorer(self):
        print("self.players when select scorer is called: ", self.players)
        defenders = [player for player in self.players if player.position == "Defender"]
        attackers = [player for player in self.players if player.position == "Attacker"]

        if random.choice(range(100)) < 70:
            scorer = random.choice(attackers)
        else:
            scorer = random.choice(defenders)

        return scorer