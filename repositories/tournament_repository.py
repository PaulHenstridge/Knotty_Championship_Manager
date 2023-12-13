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
    tourney_id = result[0]["id"]

    teams = tournament.teams
    if teams:
        for team in teams:
            sql = """
            INSERT INTO tournament_teams (tournament_id, team_id) 
            VALUES (%s, %s)
            """
            values = [tourney_id, team.id]
            run_sql(sql, values)
    
        # TODO = return a tournament so i can pass that, with id, to the template
        tournament = Tournament(teams, id=tourney_id)
        return tournament
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
        ids = run_sql(sql, values)
        teams = []
        for id_pair in ids:
            team = team_repository.select(id_pair[1])
            teams.append(team)
        # if theres a value for winner id, use it to get team, else leave it as None
        winner = None if not result["winner_id"] else team_repository.select(id)
        completed = result["completed"]
        
        tournament = Tournament(teams, winner, completed, id_pair[0])
        return tournament

# update winner of tournament
def update(tournament):
    sql = """UPDATE tournaments SET winner_id = %s, completed = %s WHERE id = %s"""
    values = [tournament.winner.id, True, tournament.id]
    run_sql(sql, values)



# delete all