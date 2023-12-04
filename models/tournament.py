import random

from models.match import Match


class Tournament:
    def __init__(self, teams, winner=None, completed=False, id=None):
        self.teams = teams
        self.winner = winner
        self.completed = completed
        self.id = id
        
        self.matches = []


    def run_tourney(self, teams):
        for team in teams:
            print(team.name)
        if len(teams) > 1:
            random.shuffle(teams)
            this_round = []
            for i in range(0, len(teams), 2):
                match = Match(teams[i], teams[i+1], False)
                this_round.append(match)
                self.matches.append(match)
            new_teams = []
            for match in this_round:
                match.play()
                new_teams.append(match.winner)

            return self.run_tourney(new_teams)
        else:
            self.winner = teams[0]
            self.winner.cup_wins +=1
            self.completed = True
            return self.winner
        
        

    