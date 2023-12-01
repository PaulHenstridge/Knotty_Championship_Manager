from db.run_sql import run_sql

from models.team import Team
from models.tournament import Tournament
import repositories.team_repository as team_repository


# create new tournament
def save(tournament):
    sql = """
    INSERT INTO tournaments (winner_id, completed) 
    VALUES (%s, %s)
    RETURNING id
    """
    values = [None, 'f']
    result = run_sql(sql, values)
    print("REEESUlT-->", result)
    tourney_id = result[0]["id"]
    print("Toornamint 19 repo", dir(tournament))

    print("Tournament object:", tournament)
    print("Tournament teams property:", tournament.teams)
    print("Type of tournament.teams:", type(tournament.teams))

    teams = tournament.teams
    print("TTEEAAMMSSSS", teams)
    if teams:
        for team in teams:
            sql = """
            INSERT INTO tournament_teams (tournament_id, team_id) 
            VALUES (%s, %s)
            """
            values = [tourney_id, team.id]
            run_sql(sql, values)
    else:
        print("No teams found in tournament object passed to save()")
# view all tournaments



# select a tournament by id
def select(id):
    tournament = None
    sql = "SELECT * FROM tournaments WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        sql = "SELECT * FROM tournament_teams WHERE tournament_id = %s"
        values = [result["id"]]
        team_ids = run_sql(sql, values)
        teams = []
        for id in team_ids:
            team = team_repository.select(id)
            teams.append(team)
        winner = result["winner"]
        completed = result["completed"]
        
        tournament = Tournament(teams, winner, completed, id)
        return tournament

# update winner of tournament
def update(tournament):
    sql = """UPDATE tournaments SET winner_id = %s, completed = %s WHERE id = %s"""
    values = [tournament.winner.id, True, tournament.id]
    run_sql(sql, values)



# delete all