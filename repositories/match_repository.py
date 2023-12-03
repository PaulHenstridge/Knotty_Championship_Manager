from db.run_sql import run_sql

from models.team import Team
from models.match import Match

import repositories.team_repository as team_repository

# TODO - refactor save() to accept a match object - see trnsfer repo
# create a new match
def save(team1_id, team2_id):
    match = None
    sql = """
    INSERT INTO matches (team1_id, team2_id, completed, winner_id) 
    VALUES (%s,%s,%s,%s)
    RETURNING id
    """
    values = [team1_id, team2_id, "f", None]

    team1 = team_repository.select(team1_id)
    team2 = team_repository.select(team2_id)
    print("*** players in team at L21 match repo***", team1.players,)

    result = run_sql(sql, values)
    return Match(team1, team2, False, None, result[0]["id"])



# view all matches
def select_all():
    matches = []

    sql = "SELECT * FROM matches"
    results = run_sql(sql)

    for result in results:
        team1 = team_repository.select(result["team1_id"])
        team2 = team_repository.select(result["team2_id"])
        winner = team_repository.select(result["winner_id"])
        match = Match(team1, team2, result["completed"], winner, result["id"])

        matches.append(match)
    return matches


# view matches by team id
def select_by_team(id):
    matches = []
    sql = "SELECT * FROM matches WHERE team1_id = %s OR team2_id = %s"
    values = [id, id]
    results = run_sql(sql, values)

    for result in results:
        team1 = team_repository.select(result["team1_id"])
        team2 = team_repository.select(result["team2_id"])
        winner = team_repository.select(result["winner_id"])
        match = Match(team1, team2, result["completed"], winner, id=result["id"])
        matches.append(match)
    return matches


# view an individual match
def select(id):
    match = None
    sql = "SELECT * FROM matches WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        team1 = team_repository.select(result["team1_id"])
        team2 = team_repository.select(result["team2_id"])
        winner = team_repository.select(result["winner_id"])
        match = Match(team1, team2, result["completed"], winner, id=id)
    return match


# update a match after the result is known
def update(match):
    sql = """UPDATE matches SET (completed, winner_id) = ('t', %s)
    WHERE id = %s"""
    values = [match.winner.id, match.id]
    run_sql(sql, values)


# delete all matches
def delete_all():
    sql = "DELETE FROM matches"
    run_sql(sql)
