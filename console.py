import repositories.team_repository as team_repository
import repositories.match_repository as match_repository
from models.team import Team
import pdb

# team_repository.save(Team("Ulbster", 52, 66, 91, 5))
# team_repository.save(Team("Latheron", 92, 87, 32, 5))
# team_repository.save(Team("Watten", 32, 66, 32, 5))
# team_repository.save(Team("Canisbay", 52, 66, 77, 3))

# all_teams = team_repository.select_all()
# for team in all_teams:
#     print(team.name, team.wins)

team1 = team_repository.select(1)
team2 = team_repository.select(2)
team3 = team_repository.select(3)
team4 = team_repository.select(4)
team5 = team_repository.select(5)
team6 = team_repository.select(6)
team7 = team_repository.select(7)

match_repository.delete_all()

match1 = match_repository.save(team1, team3)
match2 = match_repository.save(team3, team2)
match3 = match_repository.save(team4, team2)
match4 = match_repository.save(team3, team5)
match5 = match_repository.save(team6, team1)
match6 = match_repository.save(team7, team5)
match7 = match_repository.save(team4, team6)


# all_matches = match_repository.select_all()
# for match in all_matches:
#     print("id: ", match.id, match.team1.name, " v ", match.team2.name)

match_repository.select_by_team(2)
