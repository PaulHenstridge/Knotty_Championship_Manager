import random
from utils.action_reports import *

from models.player import Player

class Match:
    def __init__(self, team1, team2, completed=False, winner=None, id=None):
        self.team1 = team1
        self.team2 = team2
        self.completed = completed
        self.winner = winner
        self.id = id
        self.match_score = [0, 0]
        self.penalties = False
        self.report = []

    def play(self):
        scorers = []
        teams = [ self.team1, self.team2]
        opportunities = self.calc_opportunities()

        self.team1.matches_played += 1
        self.team2.matches_played += 1
        
        while opportunities[0] or opportunities[1]:
            idx = random.randint(0,1)
            if not opportunities[idx]:
                idx = idx ^ 1 
            opportunities[idx] -=1

            is_goal, goal_scorer = self.attempt_on_goal(teams[idx], teams[idx^1], idx)
            if isinstance(goal_scorer, Player):
                scorers.append(goal_scorer)

            self.generate_report(teams[idx], teams[idx^1], is_goal, goal_scorer)

        self.handle_draw()

        self.winner = self.declare_winner()
        self.winner.wins += 1
        self.completed = True
        return scorers


    def calc_opportunities(self):
        return [round((self.team1.attack + self.team1.defence) / 10),
                 round((self.team2.attack + self.team2.defence) / 10)]


    def attempt_on_goal(self,attacking_team, defending_team, idx):
            chance_of_scoring = 50 + (attacking_team.attack - defending_team.defence)
            if chance_of_scoring < 5:
                chance_of_scoring = 5
            if chance_of_scoring > 95:
                chance_of_scoring = 95

            shot = random.random() * 100
            if shot < chance_of_scoring:
                self.match_score[idx] += 1
                scorer = attacking_team.select_scorer() 

                return True, scorer
            else:
                return False, None
            

    def generate_report(self, team, other_team, is_goal, goal_scorer):
        if is_goal:
            message = random.choice(score_reports).format(
                team_name=team.name,
                other_team_name=other_team.name,
                score=self.match_score,
                scorer=goal_scorer.name
            )
        else:
            message = random.choice(miss_reports).format(
                team_name=team.name, 
                other_team_name=other_team.name)

        self.report.append(message)
        

    def handle_draw(self):
         # draw setled by penalties
        if self.match_score[0] == self.match_score[1]:
            self.match_score[round(random.random())] += 1
            self.penalties = True


    def declare_winner(self):
        return self.team1 if self.match_score[0] > self.match_score[1] else self.team2

    