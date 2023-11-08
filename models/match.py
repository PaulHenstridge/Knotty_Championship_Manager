import random
import math
from itertools import zip_longest
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

        # put opportunities in a list and teams in another list.
        opportunities = self.calc_opportunities()
        teams = [ self.team1, self.team2]

        print("team1:", opportunities[0], "team2:", opportunities[1])



        while opportunities[0] and opportunities[1]:
            #randomly generate an index 0 or 1. 
            idx = random.randint(0,1)
             # if opportunites for returned index are none, try other index, 
            if not opportunities[idx]:
                idx ^ 1 # using XOR operator

                # use index to decrement opportunities
            opportunities[idx] -=1
                # and call attempt_on_goal(). 
            is_goal = self.attempt_on_goal(teams[idx], teams[idx^1])

            
            self.generate_report(self.team1, self.team2, is_goal)



        # call generate_report() on each attempt, so reports are created in order


        # for opportunity in range(round(team1_opportunities)):
        #     chance_of_scoring = 50 + (self.team1.attack - self.team2.defence)
        #     if chance_of_scoring < 5:
        #         chance_of_scoring = 5
        #     if chance_of_scoring > 95:
        #         chance_of_scoring = 95

        #     shot = random.random() * 100
        #     if shot < chance_of_scoring:
        #         self.match_score[0] += 1
        #         self.generate_report(self.team1, self.team2, True)
        #     else:
        #         self.generate_report(self.team1, self.team2, False)

        # for opportunity in range(round(team2_opportunities)):
        #     chance_of_scoring = 50 + (self.team2.attack - self.team1.defence)
        #     if chance_of_scoring < 5:
        #         chance_of_scoring = 5
        #     if chance_of_scoring > 95:
        #         chance_of_scoring = 95

        #     shot = random.random() * 100
        #     if shot < chance_of_scoring:
        #         self.match_score[1] += 1
        #         self.generate_report(self.team2, self.team1, True)
        #     else:
        #         self.generate_report(self.team2, self.team1, False)

        # print("match score", self.match_score)


        self.handle_draw()

        winner = self.declare_winner()


        winner.wins += 1
        self.winner = winner
        self.completed = True
        # random.shuffle(self.report)
        # split report at length of team1_opportunities, into 2 lists
        # list1 = self.report[: math.floor(team1_opportunities)]
        # list2 = self.report[math.ceil(team1_opportunities) :]

        # self.report = [
        #     item
        #     for pair in zip_longest(list1, list2)
        #     for item in pair
        #     if item is not None
        # ]

        # classic alternative to above list comprehension
        # shuffled_list = []
        # for pair in zip_longest(list1, list2):
        #     for item in pair:
        #         if item is not None:
        #             shuffled_list.append(item)

    def generate_report(self, team, other_team, is_goal):
        if is_goal:
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


    def calc_opportunities(self):
        
        return [(self.team1.attack + self.team1.defence) / 10, (self.team2.attack + self.team2.defence) / 10]

        # t1_advantage = self.team1.attack - self.team2.defence
        # t2_advantage = self.team2.attack - self.team1.defence
        # print("t1/t2 advantage", t1_advantage, t2_advantage)
        # # if advantage is <=0 default to 3 lucky chances
        # t1, t2 = t2_advantage*-1 if  t1_advantage <= 0 else t1_advantage , t1_advantage*-1 if t2_advantage <= 0 else t2_advantage
        # #  if advantage is over 10, team gets 10 + 20% of the remainder
        # return t1 if t1 < 10 else math.ceil(10 + (t1-10) / 5), t2 if t2 < 10 else math.ceil(10 + (t2 - 10)/5)

    def attempt_on_goal(self,attacking_team, defending_team):
            chance_of_scoring = 50 + (attacking_team.attack - defending_team.defence)
            if chance_of_scoring < 5:
                chance_of_scoring = 5
            if chance_of_scoring > 95:
                chance_of_scoring = 95

            shot = random.random() * 100
            if shot < chance_of_scoring:
                self.match_score[0] += 1
                return True
            else:
                return False
        
    def handle_draw(self):
                # draw setled by penalties
        if self.match_score[0] == self.match_score[1]:
            self.match_score[round(random.random())] += 1
            self.penalties = True

    def declare_winner(self):
        return self.team1 if self.match_score[0] > self.match_score[1] else self.team2

    