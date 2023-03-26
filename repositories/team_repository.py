from db.run_sql import run_sql

from models.team import Team


# add a team to the league
def save(team):
    sql = """
    INSERT INTO teams (name, attack, defence, matches_played, wins) 
    VALUES (%s, %s, %s, %s, %s)
    RETURNING id;
    """
    values = [team.name, team.attack, team.defence, team.matches_played, team.wins]
    results = run_sql(sql, values)
    team.id = results[0]["id"]


# show all teams in league
def select_all():
    teams = []
    sql = "SELECT * FROM teams"
    results = run_sql(sql)
    for result in results:
        team = Team(
            result["name"],
            result["attack"],
            result["defence"],
            result["matches_played"],
            result["wins"],
            result["id"],
        )
        teams.append(team)
    return teams


# show an individual team by id
def select(id):
    team = None
    sql = """
        SELECT * FROM teams WHERE id = %s
    """
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        team = Team(
            result["name"],
            result["attack"],
            result["defence"],
            result["matches_played"],
            result["wins"],
            result["id"],
        )
    return team


# remove a team from the league
def delete(id):
    sql = """
    DELETE FROM teams WHERE id = %s
    """
    values = [id]
    run_sql(sql, values)


# edit/update a team


def update(team):
    sql = """
    UPDATE teams SET (name, attack, defence, matches_played, wins) = (%s,%s,%s,%s, %s)
    WHERE id = %s
    """
    values = [
        team.name,
        team.attack,
        team.defence,
        team.matches_played,
        team.wins,
        team.id,
    ]


# update team stats after match result is known
def update_stats(team):
    sql = """
    UPDATE teams SET (matches_played, wins) = (%s, %s)
    WHERE id = %s
    """
    values = [team.matches_played, team.wins, team.id]
    run_sql(sql, values)


# delete all teams from the league
def delete_all():
    sql = "DELETE FROM teams"
    run_sql(sql)
