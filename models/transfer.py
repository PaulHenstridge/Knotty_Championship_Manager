from enum import Enum

class _TransferStatus(Enum):  # Prefixed with an underscore to indicate private use
    PENDING = "pending"
    ACCEPTED = "accepted"
    DECLINED = "declined"

class Transfer:
    def __init__(self, player, team_from, team_to, transfer_fee, id = None):
        self.player = player
        self.team_from = team_from
        self.team_to = team_to
        self.transfer_fee  = transfer_fee
        self.id = id

        self.status = _TransferStatus.PENDING

    def confirm(self):
        self.status = _TransferStatus.ACCEPTED
        # update team_id on player
        self.player.team_name = self.team_to.name
        self.player.team_id = self.team_to.id
        # update bank_balance on both teams
        self.team_from.bank_balance += self.transfer_fee
        self.team_to.bank_balance -= self.transfer_fee
        # return player and teams to be updated in DB  < necessary...?
        return self.player, self.team_from, self.team_to
        
       

    def decline(self):
        self.status = _TransferStatus.DECLINED

    def nogotiate(self, new_amount):
        self.transfer_fee = new_amount
        self.status = _TransferStatus.PENDING