class Player:
    def __init__(self, name, position, skill_level, team_name, team_id, id=None):
        self.name = name 
        self.position = position
        self.skill_level = skill_level
        self.team_name = team_name
        self.team_id = team_id
        self.id = id
        self.value = self.skill_level  *12.25

    def train(self):
        #self.skill_level += some_value
        # TODO-  also add stamina/health.  health reduces when player plays or trains.
        # skill reduces slowly over time. 
        #  manager must train enough to improve squad without tiring too much

        pass

    # add self.selected to each instance, and a method to toggle it true or false
    # restrict to max of e.g 7 selected players. when a game is called, only selected players 
    # are taken into account for team scores.