from db.run_sql import run_sql

from models.team import Team
from models.match import Match

import repositories.team_repository as team_repository


# create a new match
def save(team1, team2):
    match = None
    sql = """
    INSERT INTO matches (team1_id, team2_id, completed, winner_id) 
    VALUES (%s,%s,%s,%s)
    RETURNING id
    """
    values = [team1.id, team2.id, "f", None]

    result = run_sql(sql, values)
    return Match(team1, team2, False, None, result[0]["id"])
    # TODO - increment matches played & won
    # make play_match() method on the match class
    # return a Match object above?


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
#  TODO - this not returning anything - WHY?
def select_by_team(id):
    matches = []
    sql = "SELECT * FROM matches WHERE team1_id = %s OR team2_id = %s"
    values = [id, id]
    results = run_sql(sql, values)

    for result in results:
        team1 = team_repository.select(result["team1_id"])
        team2 = team_repository.select(result["team2_id"])
        winner = team_repository.select(result["winner_id"])
        match = Match(team1, team2, result["completed"], winner)
        matches.append(match)
    return matches


# view an individual match


def select(id):
    match = None
    sql = "SELECT * FROM matches WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)

    if result:
        team1 = team_repository.select(result["team1_id"])
        team2 = team_repository.select(result["team2_id"])
        winner = team_repository.select(result["winner_id"])
        match = Match(team1, team2, result["completed"], winner)
    return match


# update a match after the result is known


def update(match, winner):
    sql = """UPDATE matches SET (completed, winner_id) = ('t', %s)
    WHERE id = %s"""
    values = [winner.id, match.id]
    run_sql(sql, values)


# delete all matches
def delete_all():
    sql = "DELETE FROM matches"
    run_sql(sql)
