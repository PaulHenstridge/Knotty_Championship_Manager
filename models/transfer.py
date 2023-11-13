class Transfer:
    def __init__(self, player, team_from, team_to, transfer_fee, id = None):
        self.player = player
        self.team_from = team_from
        self.team_to = team_to
        self.transfer_fee  = transfer_fee
        self.id = id

        self.accepted = None

    def confirm(self):
        # update team_id on player
        # update bank_balance on both teams
        self.accepted = True
       

    def decline(self):
        self.Accepted = False