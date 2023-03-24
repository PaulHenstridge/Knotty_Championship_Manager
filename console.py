import repositories.team_repository as team_repository
import repositories.match_repository as match_repository
from models.team import Team
import pdb

# team_repository.save(Team("flappers", 22, 66, 32, 5))

all_teams = team_repository.select_all()
for team in all_teams:
    print(team.name, team.wins)

team1 = team_repository.select(1)
team2 = team_repository.select(2)

print(team1.id, team2.id)

match_repository.save(team1, team2)


all_matches = match_repository.select_all()
for match in all_matches:
    print(match.team1_id)
