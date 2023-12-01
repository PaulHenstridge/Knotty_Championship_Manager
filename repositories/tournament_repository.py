from db.run_sql import run_sql

from models.team import Team
import repositories.team_repository as team_repository


# create new tournament
def save(tournament):
    sql = """
    INSERT INTO tournaments (winner) 
    VALUES (%s)
    RETURNING id
    """
    values = [None]
    result = run_sql(sql, values)
    tourney_id = result[0]["id"]
    teams = tournament.teams
    for team in teams:
        sql = """
        INSERT INTO tournament_teams (tournament_id, team_id) 
        VALUES (%s, %s)
        """
    values = [tourney_id, team.id]
    run_sql(sql, values)

# view all tournaments



# select a tournament by id



# update winner of tournament



# delete all