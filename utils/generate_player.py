import random
from models.player import Player
from utils.generate_name import generate_name
from utils.generate_name import generate_local_name

def generate_player(team_name, team_id, team_type, index):
    if team_type == "local":
        name, img_url = generate_local_name()
    else:
        name, img_url = generate_name()

    position = "Attack" if index>5 else "Defence"
    skill_level = random.choice(range(12,100))
    team_name = team_name
    team_id = team_id

    return Player(name, position, skill_level,team_name, team_id, img_url)

