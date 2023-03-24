from db.run_sql import run_sql

from models.team import Team
from models.match import Match


# create a new match
def save(team1, team2):
    sql = """
    INSERT INTO matches (team1_id, team2_id, completed, winner_id) 
    VALUES (%s,%s,%s,%s)
    RETURNING id
    """
    values = [team1.id, team2.id, "f", None]

    run_sql(sql, values)

    # TODO - increment matches played & won
    # make play_match() method on the match class


# view all matches
def select_all():
    matches = []

    sql = "SELECT * FROM matches"
    results = run_sql(sql)

    for result in results:
        match = Match(
            result["team1_id"],
            result["team2_id"],
            result["completed"],
            result["winner_id"],
        )
        matches.append(match)
    return matches


# view matches by team

# view an individual match

# delete all matches
