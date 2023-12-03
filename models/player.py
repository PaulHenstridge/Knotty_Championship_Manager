import random

class Player:
    def __init__(self, name, position, skill_level, team_name, team_id, goals=0, img_url=None, id=None):
        self.name = name 
        self.position = position
        self.skill_level = skill_level
        self.team_name = team_name
        self.team_id = team_id
        self.goals = goals
        self.img_url = img_url
        self.id = id
        self.value = self.calc_value()

    def calc_value(self):
        if hasattr(self, 'value'):
            return self.value
        else:
            multiplier = random.choice(range(8,19))
            return self.skill_level * multiplier


    def train(self):
        #self.skill_level += some_value
        # TODO-  also add stamina/health.  health reduces when player plays or trains.
        # skill reduces slowly over time. 
        #  manager must train enough to improve squad without tiring too much

        pass

    # add self.selected to each instance, and a method to toggle it true or false
    # restrict to max of e.g 7 selected players. when a game is called, only selected players 
    # are taken into account for team scores.