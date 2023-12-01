from models.match import Match

class Tournament:
    def __init__(self, teams, winner=None, completed=False, id=None):
        self.teams = teams
        self.winner = winner
        self.completed = completed
        self.id = id


    def run_tourney(self, teams):
        if len(teams) > 1:
            teams.shuffle()
            matches = []
            for i in range(0, len(teams), 2):
                match = Match(teams[i], teams[i+1], False)
                matches.append(match)
            new_teams = []
            for match in matches:
                match.play()
                new_teams.append(match.winner)

            return self.run_tourney(new_teams)
        else:
            return teams[0]
        
        

    