import random
import math
from utils.action_reports import *


class Match:
    def __init__(self, team1, team2, completed, winner=None, id=None):
        self.team1 = team1
        self.team2 = team2
        self.completed = completed
        self.winner = winner
        self.id = id
        self.match_score = [0, 0]
        self.penalties = False
        self.report = []

    def play(self):
        winner = None
        self.team1.matches_played += 1
        self.team2.matches_played += 1

        team1_opportunities = (self.team1.defence + self.team1.defence) / 10
        team2_opportunities = (self.team2.defence + self.team2.defence) / 10

        for opportunity in range(round(team1_opportunities)):
            chance_of_scoring = 50 + (self.team1.attack - self.team2.defence)
            shot = random.random() * 100
            if shot > chance_of_scoring:
                self.match_score[0] += 1
                self.generate_report(self.team1, self.team2, True)
            else:
                self.generate_report(self.team1, self.team2, False)

        for opportunity in range(round(team2_opportunities)):
            chance_of_scoring = 50 + (self.team2.attack - self.team1.defence)
            shot = random.random() * 100
            if shot > chance_of_scoring:
                self.match_score[1] += 1
                self.generate_report(self.team2, self.team1, True)
            else:
                self.generate_report(self.team2, self.team1, False)
        print("match score", self.match_score)
        # draw setled by penalties
        if self.match_score[0] == self.match_score[1]:
            self.match_score[round(random.random())] += 1
            self.penalties = True

        if self.match_score[0] > self.match_score[1]:
            winner = self.team1
        else:
            winner = self.team2
        winner.wins += 1
        self.winner = winner
        self.completed = True
        # random.shuffle(self.report)

    def generate_report(self, team, other_team, goal):
        if goal:
            message = score_reports[
                math.floor(random.random() * len(score_reports))
            ].format(
                team_name=team.name,
                other_team_name=other_team.name,
                score=self.match_score,
            )
        else:
            message = miss_reports[
                math.floor(random.random() * len(miss_reports))
            ].format(team_name=team.name, other_team_name=other_team.name)

        self.report.append(message)
