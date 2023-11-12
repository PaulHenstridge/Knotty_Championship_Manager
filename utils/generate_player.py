import random
from models.player import Player
from utils.generate_name import generate_name

def generate_player(team_name, team_id, index):
    name = generate_name()
    position = "Attack" if index>5 else "Defence"
    skill_level = random.choice(range(12,100))
    team_name = team_name
    team_id = team_id

    return Player(name, position, skill_level,team_name, team_id)

