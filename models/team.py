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

    def generate_team(self):
        #loop * 10
            # new Player:
                # list of first_names and a list of second_names
                    # randomly select one from each
                #choose atacker or defender
                # random skill level
                # self.name and self.id
            # add player to DB
            # add to a List on self
        pass

    def calculate_skill_levels(self):
        # go through the List of players
            # sum the total skill for attackers and defenders
            # set self.attack , self.defence

        pass

 #  TODO - train players and improve skill ratings
