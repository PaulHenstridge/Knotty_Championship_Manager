class Match:
    def __init__(self, team1, team2, completed, winner=None, id=None):
        self.team1 = team1
        self.team2 = team2
        self.completed = completed
        self.winner = winner
        self.id = id

    def play(self):
        winner = None
        self.team1.matches_played += 1
        self.team2.matches_played += 1
        if self.team1.attack > self.team2.defence:
            winner = self.team1
        else:
            winner = self.team2
        winner.wins += 1
        self.winner = winner
        self.completed = True

    # return winner.name


# decide the winner of the match
# update relevant statistics
#
